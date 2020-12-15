"""This module handles application's environment variables"""
import os
import sys
from labm8.py import bazelutil

def check_exists(path, bazel_path: str):
  if not os.path.exists(path):
    return bazelutil.DataPath(bazel_path)
  return path

try:
  LLVM_VERSION        = os.environ['LLVM_VERSION']
  LLVM                = check_exists(os.environ['LLVM'])
  LLVM_LIB            = check_exists(os.environ['LLVM_LIB'])
  LIBCXX_HEADERS      = check_exists(os.environ['LIBCXX_HEADERS'],
                        "libcxx_{}/include/c++/v1".format("mac" if sys.platform == "darwin" else "linux")
                        )
  CLANG               = check_exists(os.environ['CLANG'],        "phd/third_party/llvm/clang")
  CLANG_FORMAT        = check_exists(os.environ['CLANG_FORMAT'], "phd/third_party/llvm/clang-format")
  CLANG_HEADERS       = check_exists(os.environ['CLANG_HEADERS'],
                        "libcxx_{}/lib/clang/6.0.0/include".format("mac" if sys.platform == "darwin" else "linux")
                        )
  CLGEN_REWRITER      = check_exists(os.environ['CLANG_REWRITER'],      "phd/deeplearning/clgen/preprocessors/clang_rewriter")
  LIBCLC              = check_exists(os.environ['LIBCLC'],              "phd/third_party/libclc/generic/include")
  DASHBOARD_TEMPLATES = check_exists(os.environ['DASHBOARD_TEMPLATES'], "phd/deeplearning/clgen/dashboard/templates")
  DASHBOARD_STATIC    = check_exists(os.environ['DASHBOARD_STATIC'],    "phd/deeplearning/clgen/dashboard/static")

  DATA_CL_INCLUDE     = check_exists(os.environ['DATA_CL_INCLUDE'], "phd/deeplearning/clgen/data/include/")
  OPENCL_H            = os.path.join(DATA_CL_INCLUDE, "opencl.h")
  SHIMFILE            = os.path.join(DATA_CL_INCLUDE, "opencl-shim.h")

  TOKEN_LISTS         = 
except Exception as e:
  raise e
  