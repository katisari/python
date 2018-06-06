import unittest

def reverseList(arr):
    for i in range(int(len(arr)/2)):
        temp = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = arr[i]
        arr[i] = temp
    return arr

def isPalindrome(arr):
    for i in range(int(len(arr)/2)):
        if arr[i] is not arr[len(arr)-1-i]:
            return False
    return True

def coins(amount):
    quarter = 0
    dime = 0
    nickel = 0
    while(amount >= 25):
        quarter += 1
        amount -= 25
    while(amount >= 10):
        dime += 1
        amount -=10
    while(amount >=5):
        nickel += 1
        amount -= 5
    return [quarter, dime, nickel, amount]

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2) + fib(n-1)
    

class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList([2,4,-3]), [-3,4,2])
    def test3(self):
        return self.assertEqual(reverseList([-1,-2]), [-2,-1])
    def test4(self):
        return self.assertEqual(reverseList([0,3,-1]), [-1,3,0])
    def test5(self):
        return self.assertEqual(reverseList([8,-3,2]), [2,-3,8])
class isPalindromeTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(isPalindrome("racecar"), True)
    def test2(self):
        return self.assertEqual(isPalindrome("rabbit"), False)
    def test3(self):
        return self.assertTrue(isPalindrome("mom"))
    def test4(self):
        return self.assertFalse(isPalindrome("headphones"))
    def test5(self):
        return self.assertTrue(isPalindrome("dad"))

class coinTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(87), [3,1,0,2])
    def test2(self):
        return self.assertEqual(coins(92), [3,1,1,2])
    def test3(self):
        return self.assertEqual(coins(10), [0,1, 0, 0])
    def test4(self):
        return self.assertEqual(coins(45), [1,2,0,0])

class factorialTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(factorial(5), 120)
    def test2(self):
        return self.assertEqual(factorial(3), 6)
    def test3(self):
        return self.assertEqual(factorial(2), 2)
    def test4(self):
        return self.assertEqual(factorial(4), 24)

class fibTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(fib(2), 1)
    def test2(self):
        return self.assertEqual(fib(3), 2)
    def test3(self):
        return self.assertEqual(fib(4), 3)


if __name__ == "__main__":
    unittest.main()
