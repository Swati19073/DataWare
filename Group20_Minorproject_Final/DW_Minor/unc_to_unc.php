<?php
    include("connection.php”);
            $unc1=$_POST['ConditionalUncertainities'];
            echo $unc1;
            
            $unc2 = $_POST['SinkUncertainities'];
            echo $unc2;
             $sql3="INSERT INTO uncertainties_to_uncertainties(uncertainty1,uncertainty2) VALUES('$unc1','$unc2')";
            if ($conn->query($sql3)== TRUE)
            {
            header("location:conditional_uncertainities.php")
            echo "Saved succesfully";
            }
            else
            echo "Error: ";
            
            
    ?>
