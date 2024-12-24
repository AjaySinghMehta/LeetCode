class Solution:
    # def decodeString(self, s: str) -> str:
    #     stack = []
    #     current_string = ""
    #     num = 0

    #     for char in s:
    #         if char.isdigit():
    #             # Build the number for repeat count
    #             num = num * 10 + int(char)
    #         elif char == "[":
    #             # Push the current context to stack
    #             stack.append((current_string, num))
    #             current_string = ""
    #             num = 0
    #         elif char == "]":
    #             # Pop and combine the repeated substring
    #             last_string, repeat_count = stack.pop()
    #             current_string = last_string + current_string * repeat_count
    #         else:
    #             # Append character to the current string
    #             current_string += char

    #     return current_string
    
    def decodeString(self, s: str) -> str:
        def decode(index):
            current_string = ""
            num = 0

            while index < len(s):
                char = s[index]
                
                if char.isdigit():
                    # Build the number for repeat count
                    num = num * 10 + int(char)
                elif char == "[":
                    # Decode the substring inside the brackets
                    substring, index = decode(index + 1)
                    current_string += num * substring
                    num = 0  # Reset the number after processing
                elif char == "]":
                    # Return the current substring and position
                    return current_string, index
                else:
                    # Append character to the current string
                    current_string += char
                
                index += 1

            return current_string, index
        
        # Decode the full string starting from index 0
        result, _ = decode(0)
        return result

        