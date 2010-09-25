(function($) {
    $.fn.prepopulate2 = function(dependencies, maxLength) {
        /*
            Depends on urlify.js
            Populates a selected field with the values of the dependent fields,
            URLifies and shortens the string. 
            dependencies - selected jQuery object of dependent fields
            maxLength - maximum length of the URLify'd string 
        */
        return this.each(function() {
            var field = $(this);

            field.data('_changed', false);
            field.change(function() {
                field.data('_changed', true);
            });

            var populate = function () {
                // Bail if the fields value has changed
                if (field.data('_changed') == true) return;
 
                var values = [];
                dependencies.each(function() {
                    if ($(this).val().length > 0) {
                        values.push($(this).val());
                    }
                });
                field.val(values.join(' '));
            };

            dependencies.keyup(populate).change(populate).focus(populate);
        });
    };
})(django.jQuery);



$(function(){
	(function($) {
	    var field = null;

	    value = $('#id_title').val();
	    if (value.length == 0) {
		    field = {
		        id: '#id_title',
		        dependency_ids: [],
		        dependency_list: [],
		        maxLength: 50
		    };
	
		    
		    field['dependency_ids'].push('#id_name');
		    field['dependency_list'].push('.name');
		    
	
		    $('.empty-form .alias').addClass('prepopulated_field');
		    $(field.id).data('dependency_list', field['dependency_list'])
		               .prepopulate2($(field['dependency_ids'].join(',')), field.maxLength);
	    }

	})(django.jQuery);
});

$(function(){
	(function($) {
	    var field = null;

	    value = $('#id_title').val();
	    if (value.length == 0) {
		    field = {
		        id: '#id_h1',
		        dependency_ids: [],
		        dependency_list: [],
		        maxLength: 50
		    };
	
		    
		    field['dependency_ids'].push('#id_name');
		    field['dependency_list'].push('.name');
		    
	
		    $('.empty-form .alias').addClass('prepopulated_field');
		    $(field.id).data('dependency_list', field['dependency_list'])
		               .prepopulate2($(field['dependency_ids'].join(',')), field.maxLength);
	    }

	})(django.jQuery);
});