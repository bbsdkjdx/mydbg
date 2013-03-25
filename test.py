from debugger import debugger

print("start debugger...")
dbg=debugger()
dbg.attach(2776)
#dbg.write_process_memory(1243628,b'\x00\x01\x02\x03')
print(dbg.read_process_memory(1243624,8))
input()
dbg.detach()