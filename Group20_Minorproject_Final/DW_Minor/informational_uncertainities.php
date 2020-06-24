<?php
include("connection.php")
?>

<html>
<title>Conditional Uncertainties</title>
<body>
<form >
<label for="dec">Select Decision </label>
<select id="s_values" name="ConditionalUncertainities">Select Conditional Uncertainity
<option value="select conditional uncertainity"> Select Conditional Uncertainity </option>

<?php
   
    
    $sql = "select * from uncertainties where edge_type='conditional' ";
    if($res = $conn->query($sql)){
        echo " ";
        while($list = $res->fetch_array(MYSQLI_ASSOC))
        {
            $cond_unc=$list["name"];?>

<option value="<?php echo $cond_unc;?>"> <?php echo $cond_unc;?></option>

<?php
    }
    }
    ?>
</select><br>
<label for="s_sink_unc">Select Sink Uncertainity   </label>
<select id="s_sink_unc" name="SinkUncertainities">Select Sink Uncertainity
<option value="select sink uncertainity"> Select Sink Uncertainity </option>

<?php
    
    
    $sql1 = "select * from uncertainties where edge_type='informational' or edge_type='functional' ";
    if($res1 = $conn->query($sql1)){
        echo " ";
        while($list1 = $res1->fetch_array(MYSQLI_ASSOC))
        {
            $sink_unc=$list1["name"];?>

<option value="<?php echo $sink_unc;?>"> <?php echo $sink_unc;?></option>

<?php
    }
    }
    ?>
</select><br>
<button type="submit" value="Save" name="unc_to_unc_save"  >Save</button>
</form>
</body>
</html>
<?php
    if (isset($_GET["ConditionalUncertainities"]) && isset($_GET["SinkUncertainities"]))
    {
        $unc1=$_GET["ConditionalUncertainities"];
        $unc2=$_GET["SinkUncertainities"];
        $sql4="select id from uncertainties where name='$unc1'";
        $res1=$conn->query($sql4);
        $res1_list=$res1->fetch_array(MYSQLI_ASSOC);
        $id1=$res1_list["id"];
        
        $sql5="select id from uncertainties where name='$unc2'";
        $res2=$conn->query($sql5);
        $res2_list=$res2->fetch_array(MYSQLI_ASSOC);
        $id2=$res2_list["id"];
        
        
        
        
         $sql3="INSERT INTO uncertainties_to_uncertainties VALUES('$id1','$id2')";
        
        if ($conn->query($sql3)== TRUE)
            echo "Saved succesfully";
        else
            echo "Error: " . $sql . "<br>" . $conn->error;
        
        
        
    }
    ?>

