# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # MIT

py_library(
    name = "keras",
    srcs = ["//third_party/py:empty.py"],
    deps = [
        requirement("keras"),
        requirement("PyYAML"),  # Implicit dependency.
        "//third_party/py/scipy",  # Implicit dependency.
        "//third_party/py/tensorflow",
    ],
)
