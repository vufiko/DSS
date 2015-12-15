# -*- coding: utf8 -*-

# Copyright (C) 2015 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

import xbmc
import xbmcgui
from ..Utils import *
from ..ImageTools import *
from ..TheMovieDB import *
from DialogBaseInfo import DialogBaseInfo
from ..WindowManager import wm
from ActionHandler import ActionHandler
from .. import VideoPlayer

PLAYER = VideoPlayer.VideoPlayer()
ch = ActionHandler()


def get_tvshow_window(window_type):

    class DialogTVShowInfo(DialogBaseInfo, window_type):

        def __init__(self, *args, **kwargs):
            super(DialogTVShowInfo, self).__init__(*args, **kwargs)
            self.type = "TVShow"
            data = extended_tvshow_info(tvshow_id=kwargs.get('tmdb_id', False),
                                        dbid=self.dbid)
            if not data:
                return None
            self.info, self.data, self.account_states = data
            if "dbid" not in self.info:
                self.info['poster'] = get_file(self.info.get("poster", ""))
            self.info['ImageFilter'], self.info['ImageColor'] = filter_image(input_img=self.info.get("poster", ""),
                                                                             radius=25)
            self.listitems = [(150, self.data["similar"]),
                              (250, self.data["seasons"]),
                              (1450, self.data["networks"]),
                              (550, self.data["studios"]),
                              (650, merge_with_cert_desc(self.data["certifications"], "tv")),
                              (750, self.data["crew"]),
                              (850, self.data["genres"]),
                              (950, self.data["keywords"]),
                              (1000, self.data["actors"]),
                              (1150, self.data["videos"]),
                              (1250, self.data["images"]),
                              (1350, self.data["backdrops"])]

        def onInit(self):
            self.get_youtube_vids("%s tv" % (self.info['title']))
            super(DialogTVShowInfo, self).onInit()
            pass_dict_to_skin(data=self.info,
                              window_id=self.window_id)
            super(DialogTVShowInfo, self).update_states()
            self.fill_lists()

        def onClick(self, control_id):
            super(DialogTVShowInfo, self).onClick(control_id)
            ch.serve(control_id, self)

        @ch.click(120)
        def browse_tvshow(self):
            self.close()
            xbmc.executebuiltin("ActivateWindow(videos,videodb://tvshows/titles/%s/)" % (self.dbid))

        @ch.click(750)
        @ch.click(1000)
        def credit_dialog(self):
            selection = xbmcgui.Dialog().select(heading=LANG(32151),
                                                list=[LANG(32009), LANG(32147)])
            if selection == 0:
                wm.open_actor_info(prev_window=self,
                                   actor_id=self.listitem.getProperty("id"))
            if selection == 1:
                self.open_credit_dialog(self.listitem.getProperty("credit_id"))

        @ch.click(150)
        def open_tvshow_dialog(self):
            wm.open_tvshow_info(prev_window=self,
                                tvshow_id=self.listitem.getProperty("id"),
                                dbid=self.listitem.getProperty("dbid"))

        @ch.click(250)
        def open_season_dialog(self):
            wm.open_season_info(prev_window=self,
                                tvshow_id=self.info["id"],
                                season=self.listitem.getProperty("season"),
                                tvshow=self.info['title'])

        @ch.click(550)
        def open_company_info(self):
            filters = [{"id": self.listitem.getProperty("id"),
                        "type": "with_companies",
                        "typelabel": LANG(20388),
                        "label": self.listitem.getLabel().decode("utf-8")}]
            wm.open_video_list(prev_window=self,
                               filters=filters)

        @ch.click(950)
        def open_keyword_info(self):
            filters = [{"id": self.listitem.getProperty("id"),
                        "type": "with_keywords",
                        "typelabel": LANG(32114),
                        "label": self.listitem.getLabel().decode("utf-8")}]
            wm.open_video_list(prev_window=self,
                               filters=filters)

        @ch.click(850)
        def open_genre_info(self):
            filters = [{"id": self.listitem.getProperty("id"),
                        "type": "with_genres",
                        "typelabel": LANG(135),
                        "label": self.listitem.getLabel().decode("utf-8")}]
            wm.open_video_list(prev_window=self,
                               filters=filters,
                               media_type="tv")

        @ch.click(1450)
        def open_network_info(self):
            filters = [{"id": self.listitem.getProperty("id"),
                        "type": "with_networks",
                        "typelabel": LANG(32152),
                        "label": self.listitem.getLabel().decode("utf-8")}]
            wm.open_video_list(prev_window=self,
                               filters=filters,
                               media_type="tv")

        @ch.click(445)
        def show_manage_dialog(self):
            manage_list = []
            title = self.info.get("TVShowTitle", "")
            if self.dbid:
                artwork_call = "RunScript(script.artwork.downloader,%s)"
                manage_list += [[LANG(413), artwork_call % ("mode=gui,mediatype=tv,dbid=" + self.dbid)],
                                [LANG(14061), artwork_call % ("mediatype=tv, dbid=" + self.dbid)],
                                [LANG(32101), artwork_call % ("mode=custom,mediatype=tv,dbid=" + self.dbid + ",extrathumbs")],
                                [LANG(32100), artwork_call % ("mode=custom,mediatype=tv,dbid=" + self.dbid)]]
            else:
                manage_list += [[LANG(32166), "RunPlugin(plugin://plugin.video.sickrage?action=addshow&show_name=%s)" % title]]
            # if xbmc.getCondVisibility("system.hasaddon(script.tvtunes)") and self.dbid:
            #     manage_list.append([LANG(32102), "RunScript(script.tvtunes,mode=solo&amp;tvpath=$ESCINFO[Window.Property(FilenameAndPath)]&amp;tvname=$INFO[Window.Property(TVShowTitle)])"])
            if xbmc.getCondVisibility("system.hasaddon(script.libraryeditor)") and self.dbid:
                manage_list.append([LANG(32103), "RunScript(script.libraryeditor,DBID=" + self.dbid + ")"])
            manage_list.append([LANG(1049), "Addon.OpenSettings(script.extendedinfo)"])
            selection = xbmcgui.Dialog().select(heading=LANG(32133),
                                                list=[item[0] for item in manage_list])
            if selection == -1:
                return None
            for item in manage_list[selection][1].split("||"):
                xbmc.executebuiltin(item)

        @ch.click(6001)
        def set_rating(self):
            if set_rating_prompt(media_type="tv",
                                 media_id=self.info["id"]):
                self.update_states()

        @ch.click(6002)
        def open_list(self):
            index = xbmcgui.Dialog().select(heading=LANG(32136),
                                            list=[LANG(32144), LANG(32145)])
            if index == 0:
                wm.open_video_list(prev_window=self,
                                   media_type="tv",
                                   mode="favorites")
            elif index == 1:
                wm.open_video_list(prev_window=self,
                                   mode="rating",
                                   media_type="tv")

        @ch.click(6003)
        def toggle_fav_status(self):
            change_fav_status(media_id=self.info["id"],
                              media_type="tv",
                              status=str(not bool(self.account_states["favorite"])).lower())
            self.update_states()

        @ch.click(6006)
        def open_rated_items(self):
            wm.open_video_list(prev_window=self,
                               mode="rating",
                               media_type="tv")

        @ch.click(132)
        def open_text(self):
            xbmcgui.Dialog().textviewer(heading=LANG(32037),
                                        text=self.info["Plot"])

        def update_states(self):
            xbmc.sleep(2000)  # delay because MovieDB takes some time to update
            _, __, self.account_states = extended_tvshow_info(tvshow_id=self.info["id"],
                                                              cache_time=0,
                                                              dbid=self.dbid)
            super(DialogTVShowInfo, self).update_states()

    return DialogTVShowInfo
