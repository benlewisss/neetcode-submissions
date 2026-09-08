class Solution:

    def __init__(self):
        self.data_sep = "#"
        self.data_marker_end = "@"

    def encode(self, strs: List[str]) -> str:
        data_markers = ""
        strings = ""

        for string in strs:
            data_markers += str(len(string)) + self.data_sep
            strings += string

        data_markers += self.data_marker_end

        output = data_markers + strings
        return output


    def decode(self, s: str) -> List[str]:

        output = []

        # First move the pointer that points to the actual data to the position after the end data of the data markers
        string_marker_pointer = 0
        while string_marker_pointer <= len(s):
            if s[string_marker_pointer] == self.data_marker_end:
                string_marker_pointer += 1
                break
            string_marker_pointer += 1

        data_marker_end = string_marker_pointer
        data_marker_pointer = 0
        curr_data_marker = ""
        while data_marker_pointer < data_marker_end:
            if s[data_marker_pointer] == self.data_sep:
                curr_string_size = int(curr_data_marker)
                if (curr_string_size <= 0):
                    output.append("")
                    curr_data_marker = ""
                    data_marker_pointer += 1
                    continue
                
                output.append(s[string_marker_pointer:string_marker_pointer + curr_string_size])

                string_marker_pointer += curr_string_size

                curr_data_marker = ""
                data_marker_pointer += 1
                continue

            curr_data_marker += s[data_marker_pointer]
            data_marker_pointer += 1

        return output