from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import ServiceRequest, ServiceRequestAttachment
from .forms import ServiceRequestForm, ServiceRequestCommentForm, ServiceRequestAttachmentForm, AttachmentForm

@login_required
def service_request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    paginator = Paginator(requests, 10)
    page = request.GET.get('page')
    requests = paginator.get_page(page)
    return render(request, 'service_requests/list.html', {'requests': requests})


@login_required
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    comment_form = ServiceRequestCommentForm()
    attachment_form = ServiceRequestAttachmentForm()
    return render(request, 'service_requests/detail.html', {
        'service_request': service_request,
        'comment_form': comment_form,
        'attachment_form': attachment_form,
    })

# service_requests/views.py

@login_required
def service_request_update(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service request updated successfully.')
            return redirect('service_requests:detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'service_requests/update.html', {
        'form': form,
        'service_request': service_request  # Add this line
    })

@login_required
def service_request_delete(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    if request.method == 'POST':
        service_request.delete()
        messages.success(request, 'Service request deleted successfully.')
        return redirect('service_requests:list')
    return render(request, 'service_requests/delete.html', {'service_request': service_request})

@login_required
def add_comment(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    if request.method == 'POST':
        form = ServiceRequestCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.service_request = service_request
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
    return redirect('service_requests:detail', pk=pk)

@login_required
def add_attachment(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    if request.method == 'POST':
        form = ServiceRequestAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.service_request = service_request
            attachment.save()
            messages.success(request, 'Attachment added successfully.')
    return redirect('service_requests:detail', pk=pk)

@login_required
def service_request_create(request):
    AttachmentFormSet = modelformset_factory(
        ServiceRequestAttachment,
        form=AttachmentForm,
        extra=1,  # Reduced from 3 to 1 to simplify the form
        max_num=5,
        can_delete=True
    )
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        formset = AttachmentFormSet(
            request.POST,
            request.FILES,
            queryset=ServiceRequestAttachment.objects.none()
        )
        
        if form.is_valid():
            try:
                # Create service request
                service_request = form.save(commit=False)
                service_request.customer = request.user
                service_request.save()

                # Handle formset only if files were uploaded
                if formset.is_valid():
                    instances = formset.save(commit=False)
                    for instance in instances:
                        if instance.file:  # Only save if file was uploaded
                            instance.service_request = service_request
                            instance.save()
                
                messages.success(request, 'Service request created successfully!')
                return redirect('service_requests:detail', pk=service_request.pk)
            
            except Exception as e:
                messages.error(request, f'Error creating service request: {str(e)}')
                return render(request, 'service_requests/create.html', {
                    'form': form,
                    'formset': formset
                })
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ServiceRequestForm()
        formset = AttachmentFormSet(queryset=ServiceRequestAttachment.objects.none())
    
    return render(request, 'service_requests/create.html', {
        'form': form,
        'formset': formset
    })