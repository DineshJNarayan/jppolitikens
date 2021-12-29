select
    s_properties.property_id , 
	comb.* 
from (
    select
        views.time_date as views_date,
        DATE_FORMAT(views.time_date, '%Y-%m') as month_format,
        views.property as views_property,
        sum(views.total_views) as views_total_views,
        sum(users.total_users) as users_total_users,
        sum(views.full_opt_in)/sum(views.total_views) as views_full_opt_in_frac,	
        sum(users.full_opt_in) as users_full_opt_in,
        sum(users.full_opt_in)/sum(users.total_users) as users_full_opt_in_frac,
        sum(views.legitimate_int_only)/sum(views.total_views) as views_legitimate_int_only_frac,
        sum(users.legitimate_int_only) as users_legit_int_only,
        sum(users.legitimate_int_only)/sum(users.total_users) as users_legitimate_int_only_frac,
        sum(views.reject_only)/sum(views.total_views) as views_reject_only_frac,	
        sum(users.reject_only)/sum(users.total_users) as users_reject_only_frac,
        sum(views.previously_opt_in)/sum(views.total_views) as views_previously_opt_in_frac, 
        sum(users.previously_opt_in)/sum(users.total_users) as users_previously_opt_in_frac	
    from views_gdpr_performance_beta as views
    left join users_gdpr_performance_beta as users
    on views.property = users.property	
    where views.time_date = users.time_date 
    and views.opt_2 like 'desktop'
    group by views.time_date, views_property
) comb, jppol_properties as s_properties 
where comb.views_property = s_properties.property_name 
and comb.views_property like '*.itwatch.dk' 
and comb.views_date between '2021-03-01' and '2021-03-31' 
order by comb.views_date, comb.views_property