$(document).ready(function(){
    $(document).on("submit","#register-form",function(e){
        e.preventDefault();
        console.log("loaded");
        var form=$('#register-form').serialize();
        $.ajax({
            url:'/postregistration',
            type:'POST',
            data:form,
            success:function(response){
                console.log(response);
                window.location.href='/login';
            }
        });
    });
    $(document).on("submit","#login-form",function(e){
        e.preventDefault();
       console.log("Loaded")
       var form=$("#login-form").serialize();
       $.ajax({
          url:'/checklogin',
          type:'POST',
          data:form,
          success:function(res){
              if(res=="error"){
                  alert("Could not login");
              }else{
                 console.log("logged in as ",res);
                 window.location.href='/';
              }
          }
       });
    });
    $(document).on('click','#logout-link',function (e){
        e.preventDefault();
        $.ajax({
            url:'/logout',
            type:'GET',
            success:function(res){
                if(res=="success"){
                    window.location.href='/login';
                }else{
                    alert("Something went wrong.");
                }
            }
        });
    });
    $(document).on("submit","#post-activity",function(e){
        e.preventDefault();
        var form=$(this).serialize();
        $.ajax({
            url:"/postactivity",
            type:"POST",
            data:form,
            success:function(res){
                console.log(res);
            }
        });
    });
});