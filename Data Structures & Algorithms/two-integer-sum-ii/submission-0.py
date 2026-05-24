class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #must be unique indices
        #can compare target values from front and back? 

        #back and front will both be indexes 

        back, front = 0, len(numbers) - 1;

        #[1,2,3,4], target = 3, output = [1,2] index based
        while front > back:
            #top check
            if target - numbers[back] < numbers[front]:
                front -= 1; 
            #bottom check: 
            elif target - numbers[front] > numbers[back]:
                back += 1; 
            elif target - numbers[front] == numbers[back]: 
                return [back + 1, front + 1]; 
            else: 
                front -= 1; 
                back += 1; 
        

