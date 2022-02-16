def test(data):
  with open("test_File.txt", "w") as nf:

    for items in data:

      for k,v in items.items():
        nf.write(str(k)+"\n")
        nf.write(str(v)+"\n")
  return "ok"