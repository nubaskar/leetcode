"""
Description:
============
- Input array would have at least 1 word
- No empty strings would be in the input array.
- The strings would be Non-Space words.
- Max size of array is 300 words.
- 1 <= Word_Size <= 20 and  Word_Size <= Max_Width
- 1 <= Max_Width <= 100

Assessment:
===========
- Max_Size_of_input_array (300) * Word_Size (20) <= 10K. 
  So, no need to worry about space efficiency.
- Time efficiency is expected. 
- Data structure: array
- Algorithm: Linear processing of words.

Approach:
========= 
Input: ["What","must","be","acknowledgment","shall","be", "playing", "very", "Good."]
Output: [
  "What   must   be", # Full-justify
  "acknowledgment  ", # Left justify
  "shall be playing",
  "very Good.      "  # Last line - left justify only
]
maxWidth = 16

Iteration 1:
~~~~~~~~~~~~
"what"
start_index = 0
current_index = 0
current_width = 0+4 <= maxWidth: true
current_width = 0+4+1

Iteration 2:
~~~~~~~~~~~~
"must"
start_index = 0
current_index = 1
current_width = 0+4+1+4 <= maxWidth: true
current_width = 0+4+1+4+1

Iteration 3:
~~~~~~~~~~~~
"be"
start_index = 0
current_index = 2
current_width = 0+4+1+4+1+2 <= maxWidth: true
current_width = 0+4+1+4+1+2+1

Iteration 4:
~~~~~~~~~~~~
"acknowledgment"
start_index = 0
current_index = 3
current_width = 0+4+1+4+1+2+1+13 <= maxWidth: false
  - process splice 0:3 => justify(splice, left/full)
    * if current_index - start_index > 1: full, else: left
  - result will be appended to output array
  - start_index = current_index
  - current_width = len("acknowledgment") 13

current_width = 13+1

Iteration 5:
~~~~~~~~~~~~
"shall"
start_index = 3
current_index = 4
current_width = 13+1+5 <= maxWidth: false
  - process splice 3:4 => justify(splice, left/full)
    * if current_index - start_index > 1: full, else: left
  - result will be appended to output array
  - start_index = current_index
  - current_width = len("shall") 5

current_width = 5+1 (if current_index < len(input_array)), else 5

Iteration 6:
~~~~~~~~~~~~
"be"
start_index = 4
current_index = 5
current_width = 5+1+2 <= maxWidth: true
current_width = 5+1+2+1 (if current_index < len(input_array)), else 5+1+2

Iteration 7:
~~~~~~~~~~~~
"playing"
start_index = 4
current_index = 6
current_width = 5+1+2+1+7 <= maxWidth: true
current_width = 5+1+2+1+7+1 (if current_index < len(input_array)), else 5+1+2+1+7

Iteration 8:
~~~~~~~~~~~~
"very"
start_index = 4
current_index = 7
current_width = 5+1+2+1+7+1+4 <= maxWidth: false
  - process splice 4:7 => justify(splice, left/full)
    * if current_index - start_index > 1: full, else: left
  - result will be appended to output array
  - start_index = current_index (7)
  - current_width = len("very") 4

current_width = 4+1 (if current_index < len(input_array)), else 4

Iteration 9:
~~~~~~~~~~~~
"Good."
start_index = 7
current_index = 8
current_width = 4+1+5 <= maxWidth: true
current_width = 4+1+5+1 (if current_index < len(input_array)), else 4+1+5

Iteration 10:
~~~~~~~~~~~~
**** Exited the loop

start_index = 7
current_index = len(input_array) = 9
current_width = 4+1+5 <= maxWidth: true - condition not required
  - process splice 7:9 => justify(splice, left)
    * Outside loop: last line: left
  - result will be appended to output array

return result
"""
class Solution:
    def justify(self, words, maxWidth, justify_type):
        lenght_of_words = len(words)

        if justify_type == "left":
            output_string = ' '.join(words)
            padding_spaces = ' ' * (maxWidth - len(output_string))
            output_string += padding_spaces
        else:
            total_spaces = maxWidth - len(''.join(words))

            default_spaces = ' ' * (total_spaces // (lenght_of_words - 1))
            mod_value = total_spaces % (lenght_of_words - 1)
            
            if mod_value:
                output_string = (default_spaces + ' ').join(words[:mod_value]) 
                output_string += default_spaces + ' '
                output_string += default_spaces.join(words[mod_value:])
            else:
                output_string = default_spaces.join(words)

        return output_string

    def fullJustify(self, words, maxWidth):
        output = []
        words_length = len(words)

        start_index = 0
        current_index = -1
        current_width = 0

        for word in words:
            current_index += 1
            current_width += len(word)

            if not current_width <= maxWidth:
                justify_type = "full" if current_index - start_index > 1 else "left"
                output_string = self.justify(words[start_index:current_index], maxWidth, justify_type)
                output.append(output_string)
                start_index = current_index
                current_width = len(word)

            if current_index < len(words):
                current_width += 1

        current_index = len(words)
        output_string = self.justify(words[start_index:current_index], maxWidth, "left")
        output.append(output_string)

        return output

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print("\n".join(Solution().fullJustify(words, maxWidth)))
    print("========")

    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    print("\n".join(Solution().fullJustify(words, maxWidth)))
    print("========")

    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print("\n".join(Solution().fullJustify(words, maxWidth)))


