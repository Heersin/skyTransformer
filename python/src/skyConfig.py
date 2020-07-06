
# only the names of encoder now
input_format_configs = [
    "origin(.txt, .origin)",
    "abc(.abc)"
]

output_format_configs = [
    "txt",
    "png"
]

input_format_map = {
    "origin" : "origin",
    "txt" : "origin",
    "text" : "origin",
    "ori" : "origin",

    "abc" : "abc",
}

output_format_map = {
    "txt" : "cmd",
    "png" : "pics",
    "jpg" : "pics"
}
