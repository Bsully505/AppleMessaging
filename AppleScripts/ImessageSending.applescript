
set Theurl to "https://bryanmessage.herokuapp.com"
set GetResURL to "https://bryanmessage.herokuapp.com/GetRes"
set GetNum to "https://bryanmessage.herokuapp.com/GetSender"
set GetText to "https://bryanmessage.herokuapp.com/GetText"
set SetFalse to "https://bryanmessage.herokuapp.com/SetFalse"
set res to (do shell script "curl " & (quoted form of GetResURL))
set delayInMin to 5
repeat
	if res is "true" then
		tell application "Messages"
			
			set PhoneNumber to (do shell script "curl " & (quoted form of GetNum))
			set targetBuddy to participant PhoneNumber
			set Message to (do shell script "curl " & (quoted form of GetText))
			send Message to targetBuddy
			
			(do shell script "curl " & (quoted form of SetFalse))
			
			delay delayInMin
			
		end tell
		
		
		
	else
		delay delayInMin
	end if
end repeat