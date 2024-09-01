class Solution(object):
    def topKFrequent(self, words, k):
        #error checking
        if not words or k<=0:
            return []
        #create dictionary
        wordsDict = {}
        for word in words:
            if word in wordsDict:
                wordsDict[word]+=1
            else:
                wordsDict[word]=1
        
        #create heap (Using negative sing with freq. is  just a trick to simulate a max-heap by using min heap ):
        heap = [(-freq,word) for word, freq in wordsDict.items()]
        heapq.heapify(heap)

        #return top k results from heap
        return [heapq.heappop(heap)[1] for _ in range(k)]

     
# Here is the pseudocode :
   
        #STEP1: Handle error cases: if the list of words is empty or k is not positive:
            # If words is empty OR k is less than or equal to 0:
            #     Return an empty list

        #STEP2: Create a dictionary to store the frequency of each word:
            # Create an empty dictionary wordsDict
            # For each word in the list words:
            #     If the word exists in wordsDict:
            #         Increment the frequency of that word by 1
            #     Else:
            #         Add the word to wordsDict with a frequency of 1
        
        #STEP3: Create a min-heap from the dictionary items (Using negative sing with freq. is  just a trick to simulate a max-heap by using min heap ):
            # Create a heap where each entry is (-frequency, word) from wordsDict
            # Transform the list into a heap

        #STEP4: Extract the top k elements from the heap and return them as a list:
            # Initialize an empty list to store results
            # For i from 1 to k:
                # Pop the smallest element from the heap (which has the largest frequency )
                # Append the word from the popped element to the results list
                # Return the results list