import pymongo
import random
from pymongo import MongoClient


def add():
    print("Enter the Details of the Patient");
    i = random.randint(5000, 19999)
    global string_glob
    name = input("Name :")
    age = input("Age :")
    weight = input("weight :")
    bodytemp = input("body temperature:")
    z = 1
    ar = []
    end = ''
    end1 = int
    while (z != 0):
        print("what is your sex ?\n1.MALE\n2.FEMALE")
        ans1 = input("\n")
        ans = ans1.upper()
        if (ans == "MALE") or (ans == "1"):

            sex = input("\n")
            ar.append(sex)
            break

        elif (ans == "FEMALE") or (ans == "2"):
            sex = input("\n")
            ar.append(sex)
            break
    while (z != 0):
        print("patient currently admitted in hospital ?\n1.YES\n2.NO ")
        ans1 = input("\n")
        ans = ans1.upper()
        if (ans == "YES") or (ans == "1"):
            print("Enter the hospital name")
            hos = input("\n")
            ar.append(hos)
            break


        elif (ans == "NO") or (ans == "2"):
            break
    while (z != 0):
        print("Do you want to add a  Disease ?\n1.YES\n2.NO ")
        ans1 = input("\n")
        ans = ans1.upper()
        if (ans == "YES") or (ans == "1"):
            print("Enter the Disease")
            dis = input("\n")
            ar.append(dis)
            break

        elif (ans == "NO") or (ans == "2"):
            break
    while (z != 0):
        print("patient currently having blood pressure ?\n1.YES\n2.NO ")
        ans1 = input("\n")
        ans = ans1.upper()
        if (ans == "YES") or (ans == "1"):
            print("Enter the last checked record:")
            bp = input("\n")

            ar.append(bp)
            break


        elif (ans == "NO") or (ans == "2"):
            break
    while (z != 0):
        print("patient currently suffering from  blood sugar ?\n1.YES\n2.NO ")
        ans1 = input("\n")
        ans = ans1.upper()
        if (ans == "YES") or (ans == "1"):
            print("patient having recent test for blood sugar ?\n1.YES\n2.NO")
            ans1 = input("\n")
            ans = ans1.upper()
            if (ans == "YES") or (ans == "1"):
                print("enter the test result:")
            bs = input("\n")

            ar.append(bs)
            break




        elif (ans == "NO") or (ans == "2"):
            break
    while (z != 0):
        print("patient having recent test for haemoglobin test ?\n1.YES\n2.NO ")
        ans1 = input("\n")
        ans = ans1.upper()
        if (ans == "YES") or (ans == "1"):
            print("Enter the test results:")
            haemo = input("\n")
            ar.append(haemo)
            break



        elif (ans == "NO") or (ans == "2"):
            break

    for s in ar:
        end = end + s + ","

    temp = list(end)

    l = len(end)

    temp[l - 1] = ''
    string_glob = "".join(temp)

    post = {"_id": i, "Name": name, "Age": age, "weight": weight, "body temperature": bodytemp,
            "blood pressure": string_glob, "blood sugar": string_glob, "haemoglobin": string_glob, "Disease": string_glob,
            "hospital": string_glob, "sex": string_glob}
    collection.insert_one(post)


def search():
    print("Enter the ID you want to search\n")
    s = int(input())
    search = {"_id": s}
    for x in collection.find(search):
        print(x)


def update():
    print("Enter the ID you want to search\n")
    s = int(input())
    s1 = str(s)
    search = {"_id": s}
    for x in collection.find(search):
        print(x)
    print(
        "Choose the field you want to edit \n 1.Name\n2.Age\n3.weight\n4.sex\n5.hospital\n6.Disease\n7. body temperature\n8. blood pressure\n9.blood sugar\n10.haemoglobin")
    inp = input("\n")
    inp1 = inp.upper()
    strr = ""
    print(inp1)
    if (inp1 == "Name") or (inp1 == "1"):
        strr = "Name"
    elif (inp1 == "AGE") or (inp1 == "2"):
        strr = "Age"
    elif (inp1 == "weight") or (inp1 == "3"):
        strr = "weight"
    elif (inp1 == "sex") or (inp1 == "4"):
        strr = "sex"
    elif (inp1 == "hospital") or (inp1 == "5"):
        strr = "hospital"
    elif (inp1 == "Disease") or (inp1 == "6"):
        strr = "Disease"
    elif (inp1 == "body temperatur") or (inp1 == "7"):
        strr = "bodytemp"
    elif (inp1 == "blood pressure") or (inp1 == "8"):
        strr = "blood pressure"
    elif (inp1 == "blood sugar") or (inp1 == "9"):
        strr = "blood sugar"
    elif (inp1 == "haemoglobin") or (inp1 == "10"):
        strr = "haemo"

    print("Enter the new %s : " % inp1)
    addr = input("\n")

    if (inp1 == "Name") or (inp1 == "1"):
        query = {"_id": s}
        st = string_glob
        newval = {"$set": {"Name": st}}
        update = collection.update_many(query, newval)
        print(update.modified_count, "documents updated.")
    elif (inp1 == "AGE") or (inp1 == "2"):
        query = {"_id": s}
        newval = {"$set": {"Age": addr}}
    elif (inp1 == "weight") or (inp1 == "3"):
        query = {"_id": s}
        newval = {"$set": {"weight": addr}}
    elif (inp1 == "sex") or (inp1 == "4"):
        query = {"_id": s}
        newval = {"$set": {"sex": addr}}
    elif (inp1 == "hospital") or (inp1 == "5"):
        query = {"_id": s}
        newval = {"$set": {"hospital": addr}}
    elif (inp1 == "Disease") or (inp1 == "6"):
        query = {"_id": s}
        newval = {"$set": {"Disease": addr}}
    elif (inp1 == "body temperature") or (inp1 == "7"):
        query = {"_id": s}
        newval = {"$set": {"bodytemp": addr}}
    elif (inp1 == "blood pressure") or (inp1 == "8"):
        query = {"_id": s}
        newval = {"$set": {"blood pressure": addr}}
    elif (inp1 == "blood sugar") or (inp1 == "9"):
        query = {"_id": s}
        newval = {"$set": {"blood sugar": addr}}
    elif (inp1 == "haemoglobin") or (inp1 == "10"):
        query = {"_id": s}
        newval = {"$set": {"haemoglobin": addr}}

    update = collection.update_many(query, newval)
    print(update.modified_count, "documents updated.")


cluster = MongoClient("mongodb+srv://AASA:AASATech@cluster1.ipkkb.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["Patient"]
collection = db["Diseases"]
print("WELCOME TO XXXX HOSPITALS")
print("AUTOMATED TAGGING SYSTEM DESIGNED BY AASA TECH\n\n")

print(
    "Choose your options from Below \n1.Add new Patient record \n2.Search for a patient record \n3.Update a record \n4.Exit")
choice = input("\n")

if (choice == "1"):
    add()
elif (choice == "2"):
    search()
elif (choice == "3"):
    update()
elif (choice == "4"):
    print("Exiting the apllication...\n Press ok to Continue")
exit()