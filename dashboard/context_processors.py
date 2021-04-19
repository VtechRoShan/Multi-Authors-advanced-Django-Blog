# ref :https://dev.to/harveyhalwin/using-context-processor-in-django-to-create-dynamic-footer-45k4
# Defining the custom var


def CustomVar(request):
    user = request.user 
    post = user.author.blog_set.all()
    post_count = post.count()
    post_active = user.author.blog_set.filter(status='active')
    post_active_count = post_active.count()
    post_pending = user.author.blog_set.filter(status='pending')
    post_pending_count = post_pending.count()
    context= {
    'user':user,
    'post':post,
    'post_count':post_count,
    'post_active':post_active,
    'post_pending':post_pending,
    'post_active_count':post_active_count,
    'post_pending_count':post_pending_count

    }
    return context

# made by Nazrul Islam Yeasin 
# Facebbok : facebook.com/yeariha.farsin
# Github : github.com/yeazin
# website : yeazin.github.io