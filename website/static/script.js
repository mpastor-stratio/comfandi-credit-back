+ function($) {
  $('.palceholder').click(function() {
    $(this).siblings('input').focus();
  });

  $('.form-control').focus(function() {
    $(this).parent().addClass("focused");
  });

  $('.form-control').blur(function() {
    var $this = $(this);
    if ($this.val().length == 0)
      $(this).parent().removeClass("focused");
  });
  $('.form-control').blur();

  // validation
  $.validator.setDefaults({
    errorElement: 'span',
    errorClass: 'validate-tooltip'
  });

  $("#formvalidate").validate({
    rules: {
      email: {
        required: true,
        minlength: 6
      },
      password: {
        required: true,
        minlength: 6
      }
    },
    messages: {
      email: {
        required: "Por favor ingresa email.",
        minlength: "Por favor ingresa un email válido."
      },
      password: {
        required: "Por favor ingresa tu contraseña para loguearte.",
        minlength: "Login o Contraseña incorrecta."
      }
    }
  });

}(jQuery);
