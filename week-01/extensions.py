def main():
    x = get_filename()
    if x.endswith(".gif"):
        print("image/gif")
    elif x.endswith("pdf"):
        print("application/pdf")
    else :
        print("application/octet-stream")
def get_filename():
   return input("File Name? ").strip().lower()
main()