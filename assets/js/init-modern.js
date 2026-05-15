/**
 * BMH Perumbavoor Modernization - Initialization Script
 * Handles Select2, Datepicker, and other dynamic components
 */

(function($) {
    "use strict";

    $(function() {
        console.log("BMH Modernization: Initializing widgets...");

        // 1. Select2 for Department Dropdown
        const $deptSelect = $('#dept-select');
        if ($deptSelect.length) {
            try {
                if ($.fn.select2) {
                    $deptSelect.select2({
                        placeholder: "Select Department",
                        allowClear: true,
                        minimumResultsForSearch: Infinity,
                        width: '100%'
                    });
                }
            } catch (e) {
                console.error("Select2 Error:", e);
            }
        }

        // 2. jQuery UI Datepicker for Enquiry Date
        const $datePicker = $("#datepicker");
        if ($datePicker.length) {
            try {
                if ($.fn.datepicker) {
                    // Destroy any previous instance just in case main.js initialized it with different options
                    if ($datePicker.hasClass('hasDatepicker')) {
                        $datePicker.datepicker('destroy');
                    }
                    
                    $datePicker.datepicker({
                        dateFormat: 'dd/mm/yy',
                        minDate: 0,
                        showAnim: "fadeIn",
                        // Force orientation to bottom left to ensure visibility
                        beforeShow: function(input, inst) {
                            setTimeout(function() {
                                inst.dpDiv.css({
                                    top: $datePicker.offset().top + $datePicker.outerHeight() + 5,
                                    left: $datePicker.offset().left
                                });
                            }, 0);
                        }
                    });
                }
            } catch (e) {
                console.error("Datepicker Error:", e);
            }
        }

        // 3. Swiper Autoplay (Client Feedback)
        // This was already handled in main.js by setting autoplay to true,
        // but we ensure consistency here if needed.
        // 3. Swiper Autoplay (Hero Banner)
        if ($(".mySwiper-banner-bmh").length) {
            var bmhSwiper = new Swiper(".mySwiper-banner-bmh", {
                slidesPerView: 1,
                loop: true,
                effect: "slide",
                speed: 1000,
                autoplay: {
                    delay: 5000,
                    disableOnInteraction: false,
                },
            });
        }

        // 4. Nearby Facilities Swiper
        if ($(".mySwiper-nearby").length) {
            var nearbySwiper = new Swiper(".mySwiper-nearby", {
                slidesPerView: 1,
                spaceBetween: 30,
                pagination: {
                    el: ".swiper-pagination",
                    clickable: true,
                },
                breakpoints: {
                    640: {
                        slidesPerView: 2,
                    },
                    992: {
                        slidesPerView: 3,
                    },
                },
                autoplay: {
                    delay: 4000,
                    disableOnInteraction: false,
                },
            });
        }
    });

})(jQuery);
