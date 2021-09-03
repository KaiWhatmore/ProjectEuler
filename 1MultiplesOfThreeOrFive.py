class MultpiplesOfThreeOrFive:
    def forLoopMethod(n) -> int:
        sum = 0
        for i in range(n):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum



print(MultpiplesOfThreeOrFive.forLoopMethod(1000))
