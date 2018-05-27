//Validate user signup information
function registerUser(){
    var reg= /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/;
    var email=document.signupform.email.value;
    var username = document.signupform.uname.value;
    var password = document.signupform.password.value;
    var cpassword = document.signupform.cpassword.value;
    if(email.length>0){
        if(reg.test(email)){
            if(username.length>0){
                if(password.length>0){
                    if(cpassword.length>0){
                        if(password === cpassword){
                                window.location.href = "index.html";
                        }
                        else{
                            document.getElementById("msg_cpass").innerHTML = "*Password does not match!";
                            document.getElementById("msg_cpass").style.color = "Red";
                            document.getElementById("msg_email").innerHTML = "";
                            document.getElementById("msg_uname").innerHTML = "";
                            document.getElementById("msg_pass").innerHTML = "";
                            document.signupform.password.focus();
                            return false;
                        }
                    }
                    else{
                        document.getElementById("msg_cpass").innerHTML = "*Please confirm your password!";
                        document.getElementById("msg_cpass").style.color = "Red";
                        document.getElementById("msg_email").innerHTML = "";
                        document.getElementById("msg_uname").innerHTML = "";
                        document.getElementById("msg_pass").innerHTML = "";
                        document.signupform.cpassword.focus();
                        return false;
                    }
                }
                else{
                    document.getElementById("msg_pass").innerHTML = "*Please enter your password!";
                    document.getElementById("msg_pass").style.color = "Red";
                    document.getElementById("msg_email").innerHTML = "";
                    document.getElementById("msg_uname").innerHTML = "";
                    document.signupform.password.focus();
                    return false;
                }
            }
            else{
                document.getElementById("msg_uname").innerHTML = "*Please enter your username!";
                document.getElementById("msg_uname").style.color = "Red";    
                document.getElementById("msg_email").innerHTML = "";
                document.signupform.uname.focus();
                return false;
            }
        }
        else{
            document.getElementById("msg_email").innerHTML = "*Invalid email address!";
            document.getElementById("msg_email").style.color = "Red";
            document.signupform.email.focus();
            return false; 
        }
    }
    else{
        document.getElementById("msg_email").innerHTML = "*Please enter your email!";
        document.getElementById("msg_email").style.color = "Red";
        document.signupform.email.focus();
        return false;
    }
}


//Validate user login detail
function loginUser(){
    var name = document.loginform.username.value;
    var pass = document.loginform.password.value;
    if(name.length>0){
        if(pass.length>0){
            if(name === "promaster" && pass === "promaster"){
                window.open("admin_dashboard.html");
            }
            else{
                window.open("user_dashboard.html");
            }
        }
        else{
            document.getElementById("login_password").innerHTML = "*Please enter your password!";
            document.getElementById("login_password").style.color = "Red";
            document.getElementById("login_username").innerHTML = "";
            document.loginform.password.focus();
            return false;
        }
    }
    else{               
        document.getElementById("login_username").innerHTML = "*Please enter your username!";
        document.getElementById("login_username").style.color = "Red";    
        document.loginform.username.focus();
        return false;
    }
}

//Get current year
function getCurrentYear(){
    var d = new Date();
    return d.getFullYear();
}

//Display filter buttons
function getFilter(){
    $(".btn_dropdown").slideToggle("slow");						   
}

//Display requests
function requestData(){
    $("#filtered_contents").show();
    $("#post_request").hide();
    $("#right_nav").hide();
}

//Post requests
function postRequest(){
    $("#post_request").show();
    $("#filtered_contents").hide();
    $("#right_nav").hide();
}