import datetime
import json

def make_journey_skeleton_z(year_z, month_z, day_z, days_z, name_z, data_z):
    ##BEGIN CHECKING DATA
    for each_day_z in data_z:
        a_short_date_z = each_day_z["a_short_date_z"]
        b_header_z = each_day_z["b_header_z"]
        c_tiktok_links_z = each_day_z["c_tiktok_links_z"]
        d_insta_links_z = each_day_z["d_insta_links_z"]
        e_youtube_links_z = each_day_z["e_youtube_links_z"]
        f_other_links_z = each_day_z["f_other_links_z"]
        g_checked_on_z = each_day_z["g_checked_on_z"]

        assert isinstance(a_short_date_z, str)
        assert len(a_short_date_z) == 9
        assert isinstance(b_header_z, list)
        assert isinstance(c_tiktok_links_z, list)
        assert isinstance(d_insta_links_z, list)
        assert isinstance(e_youtube_links_z, list)
        assert isinstance(f_other_links_z, list)
        assert isinstance(g_checked_on_z, str)

    ##END CHECKING DATA
    all_dates_z = []
    template_z = []
    template_reversed_z = []
    date_z = datetime.datetime(year_z, month_z, day_z, 12)
    for day_count_z in range(days_z + 1):
        tag_z = ""
        if day_count_z == 0:
            pass
        else:
            short_date_z = str(date_z)[:7] + str(date_z)[8:10]
            short_date_z = short_date_z.replace("-", "_")
            tag_z = "day_{}_{}_{}_z".format(
                str(day_count_z),
                name_z,
                short_date_z
            )
            date_z += datetime.timedelta(days=1)
            if short_date_z not in all_dates_z:
                all_dates_z.append(short_date_z)
            cell_z = {
                "a_short_date_z": short_date_z,
                "b_tag_z": tag_z,
                "c_data_z": []
                }
            for each_day_z in data_z:
                a_short_date_z = each_day_z["a_short_date_z"]
                if a_short_date_z == short_date_z:
                    cell_z["c_data_z"].append(each_day_z)
            template_z.append(cell_z)
    all_dates_z = sorted(all_dates_z, reverse=True)
    for each_date_z in all_dates_z:
        for each_cell_z in template_z:
            this_cell_date_z = each_cell_z["a_short_date_z"]
            if this_cell_date_z == each_date_z:
                template_reversed_z.append(each_cell_z)
    return template_reversed_z

if __name__ == "__main__":
    assert False
