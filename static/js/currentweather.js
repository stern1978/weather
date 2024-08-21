const weather_url = `https://api.openweathermap.org/data/2.5/weather?${config.lat_lon}&units=imperial&appid=${config.weather_api}`;

fetch(weather_url)
  .then(response => response.json())
  .then(weather_data => {
    const sunrise = new Date(weather_data.sys.sunrise * 1000).toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
    const sunset = new Date(weather_data.sys.sunset * 1000).toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
    const outside_temp = Math.round(weather_data.main.temp);
    const real_feel = Math.round(weather_data.main.feels_like);
    const high = Math.round(weather_data.main.temp_max);
    const low = Math.round(weather_data.main.temp_min);
    const humidity = weather_data.main.humidity;
    const clouds = weather_data.clouds.all;
    const description = weather_data.weather[0].description.charAt(0).toUpperCase() + weather_data.weather[0].description.slice(1);
    const icon = `/static/png/${weather_data.weather[0].icon}.png`;

    let rain_hr = 0.00;
    if (weather_data.rain && weather_data.rain['1h']) {
      rain_hr = Math.round(weather_data.rain['1h'] / 25.4 * 100) / 100;
    }

    let snow_hr = 0.00;
    if (weather_data.snow && weather_data.snow['1h']) {
      const outside_temp_range = Math.floor(outside_temp / 5) * 5;
      if (outside_temp_range >= 28 && outside_temp_range < 35) {
        snow_hr = Math.round(weather_data.snow['1h'] / 25.4 * 10 * 100) / 100;
      } else if (outside_temp_range >= 20 && outside_temp_range < 28) {
        snow_hr = Math.round(weather_data.snow['1h'] / 25.4 * 15 * 100) / 100;
      } else if (outside_temp_range >= 15 && outside_temp_range < 20) {
        snow_hr = Math.round(weather_data.snow['1h'] / 25.4 * 20 * 100) / 100;
      } else if (outside_temp_range >= 10 && outside_temp_range < 15) {
        snow_hr = Math.round(weather_data.snow['1h'] / 25.4 * 30 * 100) / 100;
      } else if (outside_temp_range >= 0 && outside_temp_range < 10) {
        snow_hr = Math.round(weather_data.snow['1h'] / 25.4 * 100) / 100;
      }
    }

    console.log(sunrise);
    console.log(sunset);
    console.log(outside_temp);
    console.log(real_feel);
    console.log(high);
    console.log(low);
    console.log(humidity);
    console.log(clouds);
    console.log(description);
    console.log(icon);
    console.log(rain_hr);
    console.log(snow_hr);
  })
  .catch(error => console.log(error));