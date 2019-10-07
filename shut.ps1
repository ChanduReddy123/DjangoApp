$i=1000
for(;$i -ge 0;$i--)
{
$j=$($i/60) 
if ($j -ge 1)
{
write-host "$([math]::Round($($i/60),2)) hours remaining"
}
else
{
write-host "$i minutes remaining"
}
[System.Windows.Forms.SendKeys]::SendWait("{CAPSLOCK}")
start-sleep -Seconds 60
}