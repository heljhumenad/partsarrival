$(document).ready(function() {
  $('input[name="date_arrival"]').daterangepicker({
    singleDatePicker: true,
    timePicker: true,
    locale: {
      format: "M/D/YYYY hh:mm A",
      cancelLabel: "Cancel"
    }
  });
});

$(document).ready(function() {
  $("._dashboard p").addClass("text-white");
});
