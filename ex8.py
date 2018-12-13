formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one","Two","three","four")
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
    "I hand this thing",
    "That could you type up right",
    "But it didn't sing",
    "So i said good night."
    )