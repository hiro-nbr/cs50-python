from calculator import square
def test_assert():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    #در پایتون اسرت برای بررسی سلامت یک شرط در زمان اجرا و ایجاد خطای اسرتیشن ارور اگر شرط نادرست باشد استفاده میشود 