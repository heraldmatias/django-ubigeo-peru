function getProvincias(id,value_provincia,value_distrito){
	var provincia = $("#id_ubigeo_1");
	provincia.find('option').remove();
	provincia.append("<option value='' selected>---------</option>");
	$.getJSON('/ubigeo/provincia/json/?r='+id, function(data){
		$.each(data, function(key,value){
			if(key == 0){
				if(value_provincia != null)
					getDistritos(value_provincia,value_distrito);
				else 
					getDistritos(value.pk,value_distrito);
			}
			if(value_provincia == value.pk)
				provincia.append("<option value='"+value.pk+"' selected>"+value.fields.name+"</option>");
			else
				provincia.append("<option value='"+value.pk+"'>"+value.fields.name+"</option>");
			});
		});
}

function getDistritos(id,value_distrito){
	var distrito = $("#id_ubigeo_2");
	distrito.find('option').remove();
	distrito.append("<option value='' selected>---------</option>");
	$.getJSON('/ubigeo/distrito/json/?d='+id, function(data){
		$.each(data, function(key,value){
			if(value_distrito == value.pk)
				distrito.append("<option value='"+value.pk+"' selected>"+value.fields.name+"</option>");
			else
				distrito.append("<option value='"+value.pk+"'>"+value.fields.name+"</option>");
			});
		});
}
