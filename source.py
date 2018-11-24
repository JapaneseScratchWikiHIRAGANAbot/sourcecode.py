import mw_api_client as mwc
from pykakasi import kakasi,wakati
wp = mwc.Wiki("https://ja.scratch-wiki.info/w/api.php")
wp.login("T-taku@T-takumini", "pass")
sandbox = wp.page('記事')#記事
contents = sandbox.read()
kakasi = kakasi()
kakasi.setMode("J","H")
text = (contents)
conv = kakasi.getConverter()#ひらがな化
print(conv.do(text))
title = (conv.do(sandbox))
contents = text
summary = "ボットによる作業:ページのひらがな化"
sandbox.edit(contents, summary)
page.replace("{{ひらがなヘッダ}}", "{{ひらがなページ|" + title + }})


