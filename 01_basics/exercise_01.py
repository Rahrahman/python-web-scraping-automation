import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

"""
=============================================================================
অনুশীলনী ১: ভ্যারিয়েবল ও ক্যালকুলেশন (Exercise 1)
=============================================================================
নির্দেশনা:
নিচের ৩টি টাস্ক পূরণ করুন। কোড লেখার পর ফাইলটি রান করুন:
python 01_basics/exercise_01.py

সবগুলো টেস্ট পাস করলে আপনি "অভিনন্দন" মেসেজ দেখতে পাবেন!
=============================================================================
"""

# -------------------------------------------------------------------------
# টাস্ক ১: একটি রিমোট জবের প্রজেক্ট পেমেন্ট হিসাব করুন
# hourly_rate = 30 (প্রতি ঘণ্টার রেট $30)
# hours_worked = 40 (মোট ৪০ ঘণ্টা কাজ)
# total_earnings ভ্যারিয়েবলে মোট আয় হিসাব করে রাখুন।
# -------------------------------------------------------------------------
hourly_rate = 30
hours_worked = 40

# TODO: নিচের লাইনে মোট আয় বের করার সূত্র লিখুন (hourly_rate এবং hours_worked গুন করুন)
total_earnings = hourly_rate * hours_worked

# -------------------------------------------------------------------------
# টাস্ক ২: টাইপ কাস্টিং (Type Casting)
# user_input_price হিসেবে স্ট্রিং "250.75" দেওয়া আছে।
# converted_price ভ্যারিয়েবলে এটিকে float-এ রূপান্তর করুন।
# -------------------------------------------------------------------------
user_input_price = "250.75"

# TODO: নিচের লাইনে রূপান্তর করুন float(...) ব্যবহার করে
converted_price = float(user_input_price)  # এখানে আপনার কোড লিখুন


# -------------------------------------------------------------------------
# টাস্ক ৩: f-String দিয়ে ফরম্যাট করুন
# client_name = "TechCorp"
# formatted_summary ভ্যারিয়েবলে f-string ব্যবহার করে নিচের ফরম্যাটে স্ট্রিং তৈরি করুন:
# "Client TechCorp owes $1200" (এখানে 1200 এর জায়গায় total_earnings ভ্যারিয়েবল বসবে)
# -------------------------------------------------------------------------
client_name = "TechCorp"

# TODO: নিচের লাইনে f-string লিখুন
formatted_summary = f"cli{client_name} owes{total_earning} # এখানে আপনার কোড লিখুন

# =========================================================================
# 🧪 স্বয়ংক্রিয় টেস্ট চেকার (Automated Test Checker - DO NOT EDIT)
# =========================================================================
def run_tests():
    print("⏳ আপনার সমাধান পরীক্ষা করা হচ্ছে...\n")
    tests_passed = 0

    # Test 1
    if total_earnings == 1200:
        print("✅ টাস্ক ১ সফল: total_earnings সঠিকভাবে ১২০০ হিসাব হয়েছে।")
        tests_passed += 1
    else:
        print(f"❌ টাস্ক ১ ভুল: প্রত্যাশিত 1200, কিন্তু পাওয়া গেছে {total_earnings}")

    # Test 2
    if isinstance(converted_price, float) and converted_price == 250.75:
        print("✅ টাস্ক ২ সফল: converted_price সঠিকভাবে float(250.75) হয়েছে।")
        tests_passed += 1
    else:
        print(f"❌ টাস্ক ২ ভুল: প্রত্যাশিত 250.75 float, পাওয়া গেছে {converted_price} ({type(converted_price)})")

    # Test 3
    expected_str = "Client TechCorp owes $1200"
    if formatted_summary == expected_str:
        print("✅ টাস্ক ৩ সফল: f-string ফরম্যাটিং নিখুঁত হয়েছে।")
        tests_passed += 1
    else:
        print(f"❌ টাস্ক ৩ ভুল: প্রত্যাশিত '{expected_str}', পাওয়া গেছে '{formatted_summary}'")

    print("\n" + "=" * 45)
    if tests_passed == 3:
        print("🎉 অভিনন্দন! আপনি ক্লাস ১ এর সব টেস্ট পাস করেছেন!")
        print("পরবর্তী ধাপ: কন্ডিশনাল এবং ডিসিশন মেকিং (if/else)")
    else:
        print(f"⚠️ {3 - tests_passed} টি টাস্কে ভুল আছে। কোড ঠিক করে আবার চেষ্টা করুন।")
    print("=" * 45)

if __name__ == "__main__":
    run_tests()
