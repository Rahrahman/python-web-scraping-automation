import sys

# Windows কনসোলে বাংলা ও ইউনিকোড অক্ষর যাতে সঠিকভাবে প্রিন্ট হয়
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ---------------------------------------------------------
# ১. ভ্যারিয়েবল কী? (What is a Variable?)
# ---------------------------------------------------------
# ভ্যারিয়েবল হলো মেমোরিতে একটি নামযুক্ত পাত্র (container) যাতে কোনো মান রাখা হয়।
# পাইথনে টাইপ ডিক্লেয়ার করতে হয় না, মান অনুযায়ী পাইথন নিজে টাইপ বুঝে নেয় (Dynamic Typing)।

developer_name = "Saddad"     # str (String বা টেক্সট)
experience_years = 0          # int (Integer বা পূর্ণসংখ্যা)
hourly_rate_usd = 25.50       # float (দশমিক সংখ্যা)
is_learning_python = True     # bool (Boolean: True অথবা False)

# ---------------------------------------------------------
# ২. প্রিন্ট এবং টাইপ চেক করা (print & type)
# ---------------------------------------------------------
print("--- [১] ডাটা টাইপ পরিচিতি ---")
print("Name:", developer_name, "| Type:", type(developer_name))
print("Years of Experience:", experience_years, "| Type:", type(experience_years))
print("Hourly Rate ($):", hourly_rate_usd, "| Type:", type(hourly_rate_usd))
print("Learning Python?:", is_learning_python, "| Type:", type(is_learning_python))

# ---------------------------------------------------------
# ৩. f-Strings (আধুনিক পাইথনে স্ট্রিং ফরম্যাটিং)
# ---------------------------------------------------------
# রিমোট জবের কোডে সবসময় f-string ব্যবহার করা স্ট্যান্ডার্ড।
intro_message = f"হ্যালো! আমি {developer_name}, আমার টার্গেট রেট ${hourly_rate_usd}/hr।"
print("\n--- [২] f-String ডেমো ---")
print(intro_message)

# ---------------------------------------------------------
# ৪. টাইপ কনভার্সন বা কাস্টিং (Type Casting)
# ---------------------------------------------------------
# অনেক সময় ইনপুট থেকে ডাটা টেক্সট (str) হিসেবে আসে, সেটাকে সংখ্যায় রূপান্তর করতে হয়।
str_num = "100"
converted_int = int(str_num)      # '100' -> 100
converted_float = float(str_num)  # '100' -> 100.0

print("\n--- [৩] টাইপ কাস্টিং ---")
print(f"Original: {str_num} (Type: {type(str_num)})")
print(f"Integer : {converted_int} (Type: {type(converted_int)})")
print(f"Float   : {converted_float} (Type: {type(converted_float)})")

# ---------------------------------------------------------
# ৫. ইন্টারভিউ টেস্ট প্রশ্ন (Interview Question Preview!)
# ---------------------------------------------------------
# প্রশ্ন: নিচের কোডের আউটপুট কী হবে?
# a = "5"
# b = "10"
# print(a + b)  # আউটপুট হবে "510", কারণ দুটি স্ট্রিং জোড়া লেগেছে!
# যদি সংখ্যা যোগ করতে চাই: int(a) + int(b) = 15

print("\n--- [৪] ইন্টারভিউ কনসেপ্ট ---")
a = "5"
b = "10"
print("String যোগফল (Concat):", a + b)
print("প্রকৃত গাণিতিক যোগফল :", int(a) + int(b))
