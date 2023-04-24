# screens.rpy contains convenience functions for working with MAS screens
# and code that performs GUI related tasks such as dialog window showing.
#
# This file is part of Where is That From (see link below):
# https://github.com/friends-of-monika/mas-wtf

init python in _fom_wtf_screens:

    import store
    from store import Return


    def msgbox(text):
        """
        Convenience function for calling dialog screen with specified text.
        Shows a simple info dialog window with OK button.
        """

        renpy.invoke_in_new_context(renpy.call_screen, "dialog",
                                    message=text, ok_action=Return())


    def topic_info(ev, res):
        """
        Shows a dialog window with respective topic info received.

        IN:
            ev -> Event:
                MAS event object for the current topic.
            res -> 2-tuple or None, see search.locate_topic() output info:
                Output of search.locate_topic() with necessary info about topic.
        """

        if res is None:
            # When output is None, locating routine didn't find a trustworthy
            # script file location and therefore we cannot tell much to user
            msgbox("无法找到拥有此对话主题的文件.")

        else:
            # Obtain file path and metadata (may be None) from result parameter
            _file, metadata = res

            if metadata is None:
                # If no metadata found and file path has just one slash,
                # therefore it must be located directly in game/
                if len(_file.split("/")) == 2:
                    message = ("无法找到此话题所属的子模组, "
                               "它{{i}}可能{{/i}}是MAS本身的话题"
                               "因为它的文件被定位在"
                               "{{i}}game/{{/i}} 文件夹中: {{i}}{0}{{/i}}"
                               .format(_file))

                # Otherwise, check if it's in game/Submods
                elif (len(_file.split("/")) > 2 and
                      _file.lower().startswith("game/Submods")):
                    message = ("无法找到此话题所属的子模组, "
                               "因为它的文件被定位在其他子模组的文件夹："
                               "{{i}}game/Submods{{/i}} 文件夹中: {0}"
                               .format(_file))

                # Or else fall back to some generic message
                else:
                    message = ("无法找到此话题所属的子模组, "
                               "不过看起来它的文件在：{{i}}{0}{{/i}}."
                               .format(_file))

            else:
                # Assign metadata to vars for brevity
                submod = metadata["name"]
                version = metadata["version"]
                author = metadata["author"]

                # Make up an informative message about topic and owning submod
                message = ("看起来这个话题在 {{i}}{0} v{1},  "
                           "作者{2}{{/i}} 而且它的文件位于 "
                           "{{i}}{3}{{/i}}.".format(submod, version, author,
                                                    _file))

            # Check if topic has event prompt and it's not empty (if it's empty,
            # it is the same as event label)
            if bool(ev.prompt) and ev.prompt != ev.eventlabel:
                # Construct a message with info
                topic_title = ("这个话题的名称为 {{i}}{0}{{/i}}"
                               .format(ev.prompt))

                # If topic is random, tell so
                if ev.random:
                    topic_title += ("\n而且它{i}可能{/i}能从"
                                    "{i}我想再谈谈...{/i} 菜单中再次访问.")

                # If topic is pooled, tell so
                elif ev.pool:
                    topic_title += ("\n而且它{i}可能{/i}能从"
                                    "{i}嗨, [m_name]...{/i} 菜单中再次访问.")

                # Else just close the message with a dot if topic prompt
                # doesn't end with punctuation
                elif ev.prompt[-1] not in (".!?"):
                    topic_title += "."

                # Show message with space between submod info and topic info
                msgbox("{0}\n\n{1}".format(message, topic_title))

            else:
                msgbox(message)
