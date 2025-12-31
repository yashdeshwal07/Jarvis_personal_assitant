import os

def organize_folder(path):
    os.chdir(path)
    file = {"Documents":[], "Images":[], "Music":[], "Videos":[], "Python":[], "Misc":[]}
    for folder in file:
        if os.path.exists(folder):
            pass
        else:
            os.mkdir(folder)
        for item in os.listdir():
            ext = os.path.splitext(item)[1].lower()
            if os.path.isdir(item):
                continue
            if ext in [".pdf", ".docx"]:
                destination_path = os.path.join("Documents",item.lower())
                file["Documents"].append(item)
                os.rename(item, destination_path)
            elif ext in [".png", ".jpg", ".jpeg"]:
                destination_path = os.path.join("Images",item.lower())
                file["Images"].append(item)
                os.rename(item, destination_path)
            elif ext == ".mp3":
                destination_path = os.path.join("../music", item.lower())
                file["Music"].append(item)
                os.rename(item, destination_path)
            elif ext == ".mp4":
                destination_path = os.path.join("Videos",item.lower())
                file["Videos"].append(item)
                os.rename(item, destination_path)
            elif ext == ".py":
                destination_path = os.path.join("Python",item.lower())
                file["Python"].append(item)
                os.rename(item, destination_path)
            else:
                destination_path = os.path.join("Misc",item.lower())
                file["Misc"].append(item)
                os.rename(item, destination_path)
            for key, value in file.items():
                print(f"Moved {len(value)} files to {key}")

organize_folder("C:/Users/yashd/Messy_folder")