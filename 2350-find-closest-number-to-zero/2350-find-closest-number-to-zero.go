func findClosestNumber(nums []int) int {
    minimum := math.MaxInt64
    res := 0
    for _, num := range nums {
        absNum := abs(num)

        if absNum < minimum {
            minimum = absNum
            res = num
        } else if absNum == minimum {
            res = max(num, res)
        } 
    }

    return res
}

func abs(x int) int {
    if x >= 0 {
        return x
    }

    return -x
}