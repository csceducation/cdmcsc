def global_context(request):
    return {
        "company": "Chidhambaram",
        "user_ip": request.META.get("REMOTE_ADDR", "Unknown"),
    }
    
company = "Chidhambaram"
site_pass = "608001"
uname = "cdmcsc"