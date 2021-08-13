from h2o_wave import main, app, Q, ui, data

from FetchData import *
choices = [
ui.choice('Afghanistan', 'Afghanistan'),
ui.choice('Albania', 'Albania'),
ui.choice('Algeria', 'Algeria'),
ui.choice('Andorra', 'Andorra'),
ui.choice('Angola', 'Angola'),
ui.choice('Anguilla', 'Anguilla'),
ui.choice('Antigua and Barbuda', 'Antigua and Barbuda'),
ui.choice('Argentina', 'Argentina'),
ui.choice('Armenia', 'Armenia'),
ui.choice('Aruba', 'Aruba'),
ui.choice('Australia', 'Australia'),
ui.choice('Austria', 'Austria'),
ui.choice('Azerbaijan', 'Azerbaijan'),
ui.choice('Bahamas', 'Bahamas'),
ui.choice('Bahrain', 'Bahrain'),
ui.choice('Bangladesh', 'Bangladesh'),
ui.choice('Barbados', 'Barbados'),
ui.choice('Belarus', 'Belarus'),
ui.choice('Belgium', 'Belgium'),
ui.choice('Belize', 'Belize'),
ui.choice('Benin', 'Benin'),
ui.choice('Bermuda', 'Bermuda'),
ui.choice('Bhutan', 'Bhutan'),
ui.choice('Bolivia', 'Bolivia'),
ui.choice('Bosnia', 'Bosnia'),
ui.choice('Botswana', 'Botswana'),
ui.choice('Brazil', 'Brazil'),
ui.choice('British Virgin Islands', 'British Virgin Islands'),
ui.choice('Brunei', 'Brunei'),
ui.choice('Bulgaria', 'Bulgaria'),
ui.choice('Burkina Faso', 'Burkina Faso'),
ui.choice('Burundi', 'Burundi'),
ui.choice('Cabo Verde', 'Cabo Verde'),
ui.choice('Cambodia', 'Cambodia'),
ui.choice('Cameroon', 'Cameroon'),
ui.choice('Canada', 'Canada'),
ui.choice('Caribbean Netherlands', 'Caribbean Netherlands'),
ui.choice('Cayman Islands', 'Cayman Islands'),
ui.choice('Central African Republic', 'Central African Republic'),
ui.choice('Chad', 'Chad'),
ui.choice('Channel Islands', 'Channel Islands'),
ui.choice('Chile', 'Chile'),
ui.choice('China', 'China'),
ui.choice('Colombia', 'Colombia'),
ui.choice('Comoros', 'Comoros'),
ui.choice('Congo', 'Congo'),
ui.choice('Costa Rica', 'Costa Rica'),
ui.choice('Croatia', 'Croatia'),
ui.choice('Cuba', 'Cuba'),
ui.choice('Curaçao', 'Curaçao'),
ui.choice('Cyprus', 'Cyprus'),
ui.choice('Czechia', 'Czechia'),
ui.choice('DRC', 'DRC'),
ui.choice('Denmark', 'Denmark'),
ui.choice('Diamond Princess', 'Diamond Princess'),
ui.choice('Djibouti', 'Djibouti'),
ui.choice('Dominica', 'Dominica'),
ui.choice('Dominican Republic', 'Dominican Republic'),
ui.choice('Ecuador', 'Ecuador'),
ui.choice('Egypt', 'Egypt'),
ui.choice('El Salvador', 'El Salvador'),
ui.choice('Equatorial Guinea', 'Equatorial Guinea'),
ui.choice('Eritrea', 'Eritrea'),
ui.choice('Estonia', 'Estonia'),
ui.choice('Ethiopia', 'Ethiopia'),
ui.choice('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
ui.choice('Faroe Islands', 'Faroe Islands'),
ui.choice('Fiji', 'Fiji'),
ui.choice('Finland', 'Finland'),
ui.choice('France', 'France'),
ui.choice('French Guiana', 'French Guiana'),
ui.choice('French Polynesia', 'French Polynesia'),
ui.choice('Gabon', 'Gabon'),
ui.choice('Gambia', 'Gambia'),
ui.choice('Georgia', 'Georgia'),
ui.choice('Germany', 'Germany'),
ui.choice('Ghana', 'Ghana'),
ui.choice('Gibraltar', 'Gibraltar'),
ui.choice('Greece', 'Greece'),
ui.choice('Greenland', 'Greenland'),
ui.choice('Grenada', 'Grenada'),
ui.choice('Guadeloupe', 'Guadeloupe'),
ui.choice('Guatemala', 'Guatemala'),
ui.choice('Guinea', 'Guinea'),
ui.choice('Guinea-Bissau', 'Guinea-Bissau'),
ui.choice('Guyana', 'Guyana'),
ui.choice('Haiti', 'Haiti'),
ui.choice('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
ui.choice('Honduras', 'Honduras'),
ui.choice('Hong Kong', 'Hong Kong'),
ui.choice('Hungary', 'Hungary'),
ui.choice('Iceland', 'Iceland'),
ui.choice('India', 'India'),
ui.choice('Indonesia', 'Indonesia'),
ui.choice('Iran', 'Iran'),
ui.choice('Iraq', 'Iraq'),
ui.choice('Ireland', 'Ireland'),
ui.choice('Isle of Man', 'Isle of Man'),
ui.choice('Israel', 'Israel'),
ui.choice('Italy', 'Italy'),
ui.choice('Jamaica', 'Jamaica'),
ui.choice('Japan', 'Japan'),
ui.choice('Jordan', 'Jordan'),
ui.choice('Kazakhstan', 'Kazakhstan'),
ui.choice('Kenya', 'Kenya'),
ui.choice('Kuwait', 'Kuwait'),
ui.choice('Kyrgyzstan', 'Kyrgyzstan'),
ui.choice('Latvia', 'Latvia'),
ui.choice('Lebanon', 'Lebanon'),
ui.choice('Lesotho', 'Lesotho'),
ui.choice('Liberia', 'Liberia'),
ui.choice('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
ui.choice('Liechtenstein', 'Liechtenstein'),
ui.choice('Lithuania', 'Lithuania'),
ui.choice('Luxembourg', 'Luxembourg'),
ui.choice('MS Zaandam', 'MS Zaandam'),
ui.choice('Macao', 'Macao'),
ui.choice('Macedonia', 'Macedonia'),
ui.choice('Madagascar', 'Madagascar'),
ui.choice('Malawi', 'Malawi'),
ui.choice('Malaysia', 'Malaysia'),
ui.choice('Maldives', 'Maldives'),
ui.choice('Mali', 'Mali'),
ui.choice('Malta', 'Malta'),
ui.choice('Marshall Islands', 'Marshall Islands'),
ui.choice('Martinique', 'Martinique'),
ui.choice('Mauritania', 'Mauritania'),
ui.choice('Mauritius', 'Mauritius'),
ui.choice('Mayotte', 'Mayotte'),
ui.choice('Mexico', 'Mexico'),
ui.choice('Micronesia', 'Micronesia'),
ui.choice('Moldova', 'Moldova'),
ui.choice('Monaco', 'Monaco'),
ui.choice('Mongolia', 'Mongolia'),
ui.choice('Montenegro', 'Montenegro'),
ui.choice('Montserrat', 'Montserrat'),
ui.choice('Morocco', 'Morocco'),
ui.choice('Mozambique', 'Mozambique'),
ui.choice('Myanmar', 'Myanmar'),
ui.choice('Namibia', 'Namibia'),
ui.choice('Nepal', 'Nepal'),
ui.choice('Netherlands', 'Netherlands'),
ui.choice('New Caledonia', 'New Caledonia'),
ui.choice('New Zealand', 'New Zealand'),
ui.choice('Nicaragua', 'Nicaragua'),
ui.choice('Niger', 'Niger'),
ui.choice('Nigeria', 'Nigeria'),
ui.choice('Norway', 'Norway'),
ui.choice('Oman', 'Oman'),
ui.choice('Pakistan', 'Pakistan'),
ui.choice('Palestine', 'Palestine'),
ui.choice('Panama', 'Panama'),
ui.choice('Papua New Guinea', 'Papua New Guinea'),
ui.choice('Paraguay', 'Paraguay'),
ui.choice('Peru', 'Peru'),
ui.choice('Philippines', 'Philippines'),
ui.choice('Poland', 'Poland'),
ui.choice('Portugal', 'Portugal'),
ui.choice('Qatar', 'Qatar'),
ui.choice('Romania', 'Romania'),
ui.choice('Russia', 'Russia'),
ui.choice('Rwanda', 'Rwanda'),
ui.choice('Réunion', 'Réunion'),
ui.choice('S. Korea', 'S. Korea'),
ui.choice('Saint Helena', 'Saint Helena'),
ui.choice('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
ui.choice('Saint Lucia', 'Saint Lucia'),
ui.choice('Saint Martin', 'Saint Martin'),
ui.choice('Saint Pierre Miquelon', 'Saint Pierre Miquelon'),
ui.choice('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
ui.choice('Samoa', 'Samoa'),
ui.choice('San Marino', 'San Marino'),
ui.choice('Sao Tome and Principe', 'Sao Tome and Principe'),
ui.choice('Saudi Arabia', 'Saudi Arabia'),
ui.choice('Senegal', 'Senegal'),
ui.choice('Serbia', 'Serbia'),
ui.choice('Seychelles', 'Seychelles'),
ui.choice('Sierra Leone', 'Sierra Leone'),
ui.choice('Singapore', 'Singapore'),
ui.choice('Sint Maarten', 'Sint Maarten'),
ui.choice('Slovakia', 'Slovakia'),
ui.choice('Slovenia', 'Slovenia'),
ui.choice('Solomon Islands', 'Solomon Islands'),
ui.choice('Somalia', 'Somalia'),
ui.choice('South Africa', 'South Africa'),
ui.choice('South Sudan', 'South Sudan'),
ui.choice('Spain', 'Spain'),
ui.choice('Sri Lanka', 'Sri Lanka'),
ui.choice('St. Barth', 'St. Barth'),
ui.choice('Sudan', 'Sudan'),
ui.choice('Suriname', 'Suriname'),
ui.choice('Swaziland', 'Swaziland'),
ui.choice('Sweden', 'Sweden'),
ui.choice('Switzerland', 'Switzerland'),
ui.choice('Syrian Arab Republic', 'Syrian Arab Republic'),
ui.choice('Taiwan', 'Taiwan'),
ui.choice('Tajikistan', 'Tajikistan'),
ui.choice('Tanzania', 'Tanzania'),
ui.choice('Thailand', 'Thailand'),
ui.choice('Timor-Leste', 'Timor-Leste'),
ui.choice('Togo', 'Togo'),
ui.choice('Trinidad and Tobago', 'Trinidad and Tobago'),
ui.choice('Tunisia', 'Tunisia'),
ui.choice('Turkey', 'Turkey'),
ui.choice('Turks and Caicos Islands', 'Turks and Caicos Islands'),
ui.choice('UAE', 'UAE'),
ui.choice('UK', 'UK'),
ui.choice('USA', 'USA'),
ui.choice('Uganda', 'Uganda'),
ui.choice('Ukraine', 'Ukraine'),
ui.choice('Uruguay', 'Uruguay'),
ui.choice('Uzbekistan', 'Uzbekistan'),
ui.choice('Vanuatu', 'Vanuatu'),
ui.choice('Venezuela', 'Venezuela'),
ui.choice('Vietnam', 'Vietnam'),
ui.choice('Wallis and Futuna', 'Wallis and Futuna'),
ui.choice('Western Sahara', 'Western Sahara'),
ui.choice('Yemen', 'Yemen'),
ui.choice('Zambia', 'Zambia'),
ui.choice('Zimbabwe', 'Zimbabwe'),
]

@app('/CoronaDashboard')

async def serve(q: Q):
    n = 30

    if q.args.show_form:
        q.page.drop()

        q.page['selector'] = ui.form_card(box='1 1 3 8', items=[
            ui.label(label='Corona Analytics Data'),
            ui.dropdown(name='dropdown', label='Pick a Country', value='Sri Lanka', required=True, choices=choices),
            ui.button(name='show_inputs', label='Submit', primary=True),
        ])


    if q.args.show_data:

        if not requestCountrySummaryData(q.args.dropdown) == None:
            results = requestCountrySummaryData(q.args.dropdown)

            q.page['selector'] = ui.form_card(box='1 1 3 2', items=[
                ui.label(label='Corona Analytics Dashboard'),
                ui.text(f'{q.args.dropdown}'),
                ui.button(name='show_form', label='Back', primary=True),
            ])

            population = q.page.add('population', ui.large_stat_card(
                box='2 3 2 2',
                title="Country Population",
                value=f"{results['population']}",

                aux_value=f"",
                data=dict(qux=results['cases'], quux=results['population']),
                caption=f"Data updated at {results['updatedAt']}",
            ))

            flag = q.page['flag'] = ui.image_card(
                box='1 3 1 2',
                title=f"{results['country']}",
                path=f"{results['flag']}",
            )

            cases = q.page.add('cases', ui.large_stat_card(
                box='1 5 3 2',
                title="Total Corona Cases",
                value=f"{results['cases']}",
                aux_value= f'{  "{:.4f}".format((results["cases"] / results["population"]))   } %' ,
                data=dict(qux=results['cases'], quux=results['population']),
                caption='Percentage of Population',
            ))

            deaths = q.page.add('deaths', ui.large_stat_card(
                box='1 7 3 2',
                title="Total Corona Deaths",
                value=f"{results['deaths']}",
                aux_value=f'{"{:.4f}".format((results["deaths"] / results["cases"]))} %',
                data=dict(qux=results['cases'], quux=results['population']),
                caption='Mortality Rate',
            ))

            todayCases = q.page.add('example', ui.small_stat_card(
                box='1 9 1 2',
                title="Today Cases",
                value=f"{results['todayCases']}",
            ))

            todayDeaths = q.page.add('todayDeaths', ui.small_stat_card(
                box='2 9 1 2',
                title="Today Deaths",
                value=f"{results['todayDeaths']}",
            ))

            tests = q.page.add('tests', ui.small_stat_card(
                box='3 9 1 2',
                title="Tests",
                value=f"{results['tests']}",
            ))

            Active = q.page.add('Active', ui.large_stat_card(
                box='1 11 3 2',
                title="Total Active Cases",
                value=f"{results['active']}",
                aux_value=f'{"{:.4f}".format((results["active"] / results["cases"]))} %',
                data=dict(qux=results['active'], quux=results['cases']),
                caption='Percentage from all cases',
            ))


        else:

            q.page.drop()

            q.page['selector'] = ui.form_card(box='1 1 3 8', items=[
                ui.label(label='Corona Analytics Data'),
                ui.dropdown(name='dropdown', label='Pick a Country', value='Sri Lanka', required=True, choices=choices),
                ui.button(name='show_inputs', label='Submit', primary=True),
            ])

        if not requestDataByCountry(  q.args.dropdown  ) == None:

            cases = q.page.add('corona_cases', ui.plot_card(
                box='4 1 6 4',
                title='Total Corona Cases',
                data=data('date cases', n),
                plot=ui.plot([
                    ui.mark(type='area', x_scale='time', x='=date', y='=cases', y_min=0),
                    ui.mark(type='line', x='=date', y='=cases')
                ])
            ))

            cases.data = requestDataByCountry(  q.args.dropdown  )[0]
            deaths = q.page.add('corona_deaths', ui.plot_card(
                box='4 5 6 4',
                title='Total Corona Deaths ',
                data=data('date deaths', n),
                plot=ui.plot([
                    ui.mark(type='area', x_scale='time', x='=date', y='=deaths', y_min=0),
                    ui.mark(type='line', x='=date', y='=deaths')
                ])
            ))
            deaths.data = requestDataByCountry(  q.args.dropdown  )[1]

            recovered = q.page.add('corona_recovered', ui.plot_card(
                box='4 9 6 4',
                title='Total Corona Recovery',
                data=data('date recovery', n),
                plot=ui.plot([
                    ui.mark(type='area', x_scale='time', x='=date', y='=recovery', y_min=0),
                    ui.mark(type='line', x='=date', y='=recovery')
                ])
            ))
            recovered.data = requestDataByCountry(q.args.dropdown)[2]

        else:
            del q.page['corona_cases']
            del q.page['corona_deaths']
            del q.page['corona_recovered']

    else:
        q.page['selector'] = ui.form_card(box='1 1 3 8', items=[
            ui.label(label='Corona Analytics Dashboard'),
            ui.dropdown(name='dropdown', label='Pick a Country', value='Sri Lanka', required=True, choices=choices),
            ui.button(name='show_data', label='Submit', primary=True),
        ])

    #if not q.client.initialized:

     #   q.client.initialized = True



    await q.page.save()
