$(document).ready(function() {
  $('input[name="date_arrival"]').daterangepicker({
    singleDatePicker: true,
    timePicker: true,
    locale: {
      format: "M/D/YYYY hh:mm A",
      cancelLabel: "Cancel"
    }
  });
  $("._dashboard p").addClass("text-white");
  // modal values
  $(".read-partsnumber").each(function() {
    $(this).modalForm({
      formURL: $(this).data("id")
    });
  });
});
