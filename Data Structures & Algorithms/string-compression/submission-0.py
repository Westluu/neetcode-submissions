class Solution:
    def compress(self, chars: List[str]) -> int:
        #consective (sliding window)
        #get a window of repeating chars until hit different char
        #then append that char to s followed by length of window (if > 1)
        #repeating until we reach the end of chars

        s = ""
        l = r = 0
        while l < len(chars):
            while r < len(chars) and chars[l] == chars[r]:
                r+=1
            s += chars[l]
            window_length = r - l
            if window_length > 1:
                s += str(window_length)
            
            #reset the window
            l = r
            r = l
        
        i = 0
        while i < len(s):
            chars[i] = s[i]
            i+=1
        return i
