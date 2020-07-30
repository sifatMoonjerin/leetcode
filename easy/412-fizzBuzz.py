def fizzBuzz(nums):
    fizz = 3
    buzz = 5

    res = []

    for num in range(1, nums+1):
        if num % (fizz*buzz) == 0:
            res.append('FizzBuzz')
        elif num % fizz == 0:
            res.append('Fizz')
        elif num % buzz == 0:
            res.append('Buzz')
        else:
            res.append(str(num))

    return res


print(fizzBuzz(15))
