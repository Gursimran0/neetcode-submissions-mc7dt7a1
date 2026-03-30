func sortColors(nums []int) {
    i := 0 
    l := 0 
    r := len(nums)-1

    for i<=r{
        if nums[i] == 0{
            swap(nums,i,l)
            l++

        } else if nums[i] == 2{
            swap(nums,i,r)
            r--
            i--
        }
        i++
    }
    
}
func swap(nums []int, i int, j int){
    temp := nums[i]
    nums[i] = nums[j]
    nums[j] = temp
}
