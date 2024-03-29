$(document).ready(function() {
  $('input[name="date_arrival"]').daterangepicker({
    singleDatePicker: true,
    showDropdowns:"true",
    timePicker: true,
    drops: "up",
    minDate: moment().startOf('day'),
    locale: {
      format: "MM/DD/YYYY",
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

  $(".read-arrival").each(function() {
    $(this).modalForm({
      formURL: $(this).data("id")
    });
  });

  $(".read-advisor").each(function() {
    $(this).modalForm({
      formURL: $(this).data("id")
    });
  });

  $(".read-item-class").each(function() {
    $(this).modalForm({
      formURL: $(this).data("id")
    });
  });
  // Add modal
  // $(".create-parts").modalForm({
  //   formURL: "{% url 'partsnumber:parts_number_create_view' %}"
  // });
  // Edit partsnumber modal
});
