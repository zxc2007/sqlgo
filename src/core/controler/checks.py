import io
import os
import sys
sys.path.append(os.getcwd())
import gzip
import zlib


def page_encoding(response, action):
  try:
    page = response.read()
  except _http_client.IncompleteRead as err_msg:
    requests.request_failed(err_msg)
    page = err_msg.partial
  if response.info().get('Content-Encoding') in ("gzip", "x-gzip", "deflate"):
    try:
      if response.info().get('Content-Encoding') == 'deflate':
        data = io.BytesIO(zlib.decompress(page, -15))
      elif response.info().get('Content-Encoding') == 'gzip' or \
           response.info().get('Content-Encoding') == 'x-gzip':
        data = gzip.GzipFile("", "rb", 9, io.BytesIO(page))
      page = data.read()
      settings.PAGE_COMPRESSION = True
    except Exception as e:
      if settings.PAGE_COMPRESSION is None:
        warn_msg = "Turning off page compression."
        print(settings.print_warning_msg(warn_msg))
        settings.PAGE_COMPRESSION = False
  _ = False
  try:
    if action == "encode" and type(page) == str:
      return page.encode(settings.DEFAULT_CODEC, errors="ignore")
    else:
      return page.decode(settings.DEFAULT_CODEC, errors="ignore")
  except (UnicodeEncodeError, UnicodeDecodeError) as err:
    err_msg = "The " + str(err).split(":")[0] + ". "
    _ = True
  except (LookupError, TypeError) as err:
    err_msg = "The '" + settings.DEFAULT_CODEC + "' is " + str(err).split(":")[0] + ". "
    _ = True
    pass
  if _:
    err_msg += "You are advised to rerun with"
    err_msg += ('out', '')[menu.options.codec == None] + " option '--codec'."
    print(settings.print_critical_msg(str(err_msg)))
    raise SystemExit()