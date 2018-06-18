Import "ShanHai.lua"
Import "Cjson.lua"
// 日志路径
/* ======================================== Param */
Dim DEGREE            = 0.8
Dim def              = Array(0,0)
Dim DEBUG            = True
Dim  MyString, ModelName, mName
ModelName = Device.GetModel()
MyString = Split(ModelName, " ")
mName =  MyString(1)


Dim xy_clear        = Array(660,230)
Dim maxX = GetScreenX()
Dim maxY = GetScreenY()
Dim g_last_x = -1
Dim g_last_y = -1
Dim g_must_cancel_update_flag = True
Dim g_timeout_flag = False
Dim g_base_path = "/mnt/shared/Other/"

// 日志路径
Dim logPath = g_base_path & mName & ".log"
Dim g_result_file = g_base_path & mName & ".result"



/* ======================================== Main */
DDL "============================================="
DDL "[+] 启动任务 <淘宝联盟 V1.10> " & Date() & " " & DateTime.Format("%H:%M:%S", time()) 

DL "[+] 开始初始化."
If init() = False Then 
    DL "[X] 初始化失败."
    EndScript
End If    

MainLoop()


Function init()

    // 初始化系统
 
    // 打印 日志路径
    DL "[-] 日志路径 [" & logPath & "]"

//    waitAndTapTimeout "top500标签未高亮", def, 3 
//  
//    waitAndTapTimeout "top500", def, 5
//    
//    
//    waitAndTapTimeout "选择top1000", def, 5
//    
//    waitPicTimeout "top1000", 5
	
    init = True
    
End Function





Sub PorcessOneFile()


    Dim lines, line, listFilePath, overFilePath, listNum, indexFilePath


    listFilePath = g_base_path & mName & ".list"
    overFilePath = g_base_path & mName & ".over"
//    indexFilePath = g_base_path & mName & ".index"
	indexFilePath = g_base_path & mName & ".list"

    DDL "[-] 机型信息:" & ModelName
    
    If Dir.Exist(listFilePath) = 0 Then 
    	DDL "[X] 找不到" & listFilePath & "文件"
    	EndScript
    End If
    
    
//    If Dir.Exist(indexFilePath) = 0 Or File.LinesNumber(indexFilePath) = 0 Then 
//    	DDL "[-] 重新初始化Index文件" & indexFilePath & "文件"
//    	Dir.Copy listFilePath, indexFilePath
//    End If
//    
    If Dir.Exist(overFilePath) = 0 Then
        Dim ret
        listNum = File.LinesNumber(indexFilePath)
        DDL "[-] 加载列表. 待处理数量 [" & listNum & "]"
        lines = File.ReadLines(indexFilePath)


        For Each line In lines
        	
        	
        	If Len(LTrim(line)) > 0 Then 
        		
            	DL "[-] 开始处理行: " & line
            	
            	
    			Dim MyString, pkid, ordernumber
    			MyString = Split(line,"#")
    			pkid=MyString(0) 
    			ordernumber=MyString(1) 
            	ret = ProceOneLine(line)
        		
            	If ret = True Then 
                	DDL "[-]【"  & line & "】处理成功.."
            	Else 
            		DDL "[X]【" & line & "】 处理失败..."
            		WriteResultFile "E##" & pkid & "##异常"
//            		Exit For
            	End If
            	// 处理结束删除改行
            	Call File.DeleteLine(indexFilePath, 1)
    			DL "[-] 完成操作，返回..."
    			Do While True
        			DL "[-] 点击【返回】."
        			KeyPress "Back"
        			Delay 2000
        			waitAndTapTimeout "search_icon", def, 6
        			If g_timeout_flag = False Then 
        	 			DL "[-] 到底了不需要继续【返回】."
        				Delay 1000
            			Exit Do
        			End If
    			Loop
        	End If        
        Next
        
      
        DDL "[+] 文件处理完成对结果文件进行重命名, 重命名成 "  & overFilePath 
		Dir.Move g_result_file, overFilePath
		Delay 3000

    ElseIf Dir.Exist(overFilePath) = 1 Then 
        DDL "[-] 文件处理完成:" & overFilePath & "等待下一个任务"
        TracePrint Dir.Exist(overFilePath)
        Delay 3000
    ElseIf Dir.Exist(listFilePath) = 0 Then  
        DDL "[-] 处理文件不存在: "  & mName & ".list"
    End If
	

End Sub



Function MainLoop()
	DL "[-] 进入主循环..."

	Dim loop_times = 0
    Do While True
        DL "[-] 点击【返回】."
      ProceOneLine (1)
//    	Do While True
//
//        	If g_timeout_flag = False Then 
//        		DL "[-] 到底了不需要继续【返回】."
//        		Delay 1000
//            	Exit Do
//        	End If
        	
//    	Loop
    Loop
End Function

Function ProceOneLine(line)

    ProceOneLine = True
  
    Dim MyString, pkid, ordernumber

    Delay 5000
    Dim start_t = time()
    Dim end_t = time()
    DL "[-] 设置间隔开始时间. [" & DateTime.Format("%H:%M:%S", start_t) & "]"
    DL "[#] " & line
    
    Swipe  234,411, 239,326
	Delay 3000
    Tap 175, 291
    Delay 3000
    waitAndTapTimeout "项目介绍", def, 15
    Delay 1000
    waitAndTapTimeout "项目简介", def, 15
	Delay 3000
    DL "[-] 点击【返回】."
    KeyPress "Back"
    Delay 4000
    waitAndTapTimeout "币行情", def, 60

	
End Function




Function isChange(icon, coord)
    Dim x = -1, y = -1
    Do Until x <= 0
        FindPic coord(0), coord(1), maxX, maxY, "Attachment:" & icon & ".png", "000000", 0, DEGREE, x, y
        Delay 500
    Loop
    DB "** 画面已变更.可执行下一步操作."
    Delay 1000
End Function

Function isChangeTimeout(icon, coord, sec)

    g_timeout_flag = False

    Dim start_t = time()
    Dim end_t = time()
    DL "[-] 设置间隔开始时间. [" & DateTime.Format("%H:%M:%S", start_t) & "] 超时时间[" & sec & "] 秒"
    
    Dim x = -1, y = -1
    Do Until x <= 0
        FindPic coord(0), coord(1), maxX, maxY, "Attachment:" & icon & ".png", "000000", 0, DEGREE, x, y
        Delay 500
        
        end_t = time()
        If end_t - start_t >= sec Then 
            DL "[X] 等待画面变更 " & icon & " 秒 超时！"
            g_timeout_flag = True
            Exit Function
        End If
    Loop
    DB "** 画面已变更.可执行下一步操作."
    Delay 1000
End Function

Function waitFor(icon, coord)

    Dim resX = -1,resY = -1    
    Do Until resX > -1
        FindPic coord(0), coord(1), maxX, maxY, "Attachment:"&icon&".png","000000",0, DEGREE, resX, resY
        Delay 200
        DB "** 等待 "& icon & ",Delay 500"
    Loop
    DB "** 找到  " & icon & ": [" & resX & "," & resY & "]"

End Function

Sub checkTime(stime, d)

    Dim etime = time()
    Do Until (etime - stime) >= d
        DB "** 未达到时间, Delay 1s."
        Delay 1000
        etime = Time()
    Loop
    DB "** 达到限制时间. "
End Sub

Sub myTap(x, y)
    DB "** 点击 [" & x & "," & y & "]"
    Touch x, y, 200
End Sub

Sub DL(x)

    TracePrint x
    ShowMessage x
//    File.Append logPath, x & Chr(10)

End Sub

Sub DDL(x)

    TracePrint x
    ShowMessage x
    File.Append logPath, x & Chr(10)

End Sub

Sub DB(x)

    If DEBUG Then 
        TracePrint x
        ShowMessage x
    End If

End Sub

Function isPic(icon)

    isPic = False
    g_last_x = -1
    g_last_y = -1
    FindPic 0, 0, 0, 0, "Attachment:" & icon & ".png", "000000", 0, DEGREE, g_last_x, g_last_y
    If g_last_x > -1 Then 
        DB "** 找到目标图片 " & icon & ". [" & g_last_x & "," & g_last_y & "]"
        isPic = True
    End If

End Function

Function waitPicTimeout(icon, sec)

    g_timeout_flag = False
    g_last_x = -1
    g_last_y = -1


    Dim start_t = time()
    Dim end_t = time()
    DL "[-] 设置间隔开始时间. [" & DateTime.Format("%H:%M:%S", start_t) & "] 超时时间[" &  sec & "] 秒"

    Do Until g_last_x > -1
        FindPic 0, 0, 0, 0, "Attachment:"& icon &".png","000000",0, DEGREE, g_last_x, g_last_y
        Delay 500
    
        end_t = time()
        If end_t - start_t >= sec Then 
            DL "[X] 查找图片 " & icon & " 秒 超时"
            g_timeout_flag = True
            Exit Function
        End If
        DB "** wait for "& icon & ",delay 500"
    Loop

    DB "** 找到  " & icon & ": [" & g_last_x & "," & g_last_y & "]. Tap [" & g_last_x + 10 & "," & g_last_y + 10 & "]"

End Function


Sub waitAndTap(icon, coord)
    g_last_x = -1
    g_last_y = -1
    Do Until g_last_x > -1
        FindPic 0, 0, 0, 0, "Attachment:"& icon &".png","000000",0, DEGREE, g_last_x, g_last_y
        Delay 500
        DB "** wait for "& icon & ",delay 500"
    Loop

    DB "** 找到  " & icon & ": [" & g_last_x & "," & g_last_y & "]. Tap [" & g_last_x + 10 & "," & g_last_y + 10 & "]"
    Delay 500
    If coord(0) = 0 and coord(1) = 0 Then 
        myTap g_last_x + 10, g_last_y + 10
    Else 
        myTap coord(0), coord(1)
    End If

End Sub


Sub waitAndTapTimeout(icon, coord, sec)
    g_timeout_flag = False
    g_last_x = -1
    g_last_y = -1


    Dim start_t = time()
    Dim end_t = time()
    DL "[-] 设置间隔开始时间. [" & DateTime.Format("%H:%M:%S", start_t) & "] 超时时间[" &  sec & "] 秒"

    Do Until g_last_x > -1
        FindPic 0, 0, 0, 0, "Attachment:"& icon &".png","000000",0, DEGREE, g_last_x, g_last_y
        Delay 500
    
        end_t = time()
        If end_t - start_t >= sec Then 
            DL "[X] 查找图片 " & icon & " 秒 超时"
            g_timeout_flag = True
            Exit Function
        End If
        DB "** wait for "& icon & ",delay 500"
    Loop

    DB "** 找到  " & icon & ": [" & g_last_x & "," & g_last_y & "]. Tap [" & g_last_x + 10 & "," & g_last_y + 10 & "]"
    Delay 500
    If coord(0) = 0 and coord(1) = 0 Then 
        myTap g_last_x + 10, g_last_y + 10
    Else 
        myTap coord(0), coord(1)
    End If

End Sub


Sub waitForRes(icon_1, icon_2)

    Dim i
    For i = 1 To 120    
        //KeepCapture 
        Dim x = -1,y = -1    
    
        FindPic 0, 0, 0, 0, "Attachment:" & icon_1 & ".png", "000000", 0, DEGREE, x, y
        If x > -1 Then 
            DB "** 找到 "&icon_1
            Exit For
        End If
    
        FindPic 0, 0, 0, 0, "Attachment:" & icon_2 & ".png", "000000", 0, DEGREE, x, y
        If x > -1 Then 
            DB "** 找到 "&icon_2
            Exit For
        End If
        DB "** 未找到目标结果."
        Delay 500
    
    Next

    //ReleaseCapture

    If i >= 120 Then 
        DL "[X] 操作超时."
    End If

End Sub




Sub waitOneRes(icon_1, icon_2)

    Dim i
    waitOneRes = -1
    For i = 1 To 120    
        //KeepCapture 
        Dim x = -1,y = -1    
    
        FindPic 0, 0, 0, 0, "Attachment:" & icon_1 & ".png", "000000", 0, DEGREE, x, y
        If x > -1 Then 
            DB "** 找到1 " & icon_1
            waitOneRes = 1
            Exit For
        End If
    
        FindPic 0, 0, 0, 0, "Attachment:" & icon_2 & ".png", "000000", 0, DEGREE, x, y
        If x > -1 Then 
            DB "** 找到2 " & icon_2
            waitOneRes = 2
            Exit For
        End If
        DB "** 未找到目标结果."
        Delay 500
    
    Next

    //ReleaseCapture

    If i >= 120 Then 
        DL "[X] 操作超时."
    End If

End Sub



Sub WriteResultFile(x)

    TracePrint x
    ShowMessage x
    File.Append g_result_file, x & Chr(10)

End Sub