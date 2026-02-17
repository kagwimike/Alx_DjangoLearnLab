# Django Security Best Practices Implemented

## 1. Secure Settings

- DEBUG = False
- SECURE_BROWSER_XSS_FILTER = True
- X_FRAME_OPTIONS = "DENY"
- SECURE_CONTENT_TYPE_NOSNIFF = True
- CSRF_COOKIE_SECURE = True
- SESSION_COOKIE_SECURE = True
- SECURE_SSL_REDIRECT = True

These settings protect against XSS, clickjacking, and session hijacking.

---

## 2. CSRF Protection

All forms include:

{% csrf_token %}

This prevents Cross-Site Request Forgery attacks.

---

## 3. SQL Injection Prevention

Django ORM is used instead of raw SQL queries:

Book.objects.filter(title__icontains=query)

Django automatically parameterizes queries.

---

## 4. Input Validation

Django Forms are used to validate and sanitize user input.

---

## 5. Content Security Policy

django-csp middleware is configured to restrict external scripts and resources.
