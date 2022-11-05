$("form[name=signup_form").submit(function (e) {

	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/register",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		}
	});

	e.preventDefault();
});

$("form[name=login_form").submit(function (e) {
	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/login",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/userhome";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		}
	});

	e.preventDefault();
});


$("form[name=upload_form").submit(function (e) {

	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/uploadsnip",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/userhome";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		}
	});

	e.preventDefault();
});