import re as re_

class GeneratedsSuper(object):
    def gds_format_string(self, input_data, input_name=''):
        #return input_data
        # kusno = replace unknown characters with the right xml representation
        try:
            # straight encode 'ascii' doesn't work, I have to return it back to utf8 first
            # I returned it to utf-8, since in the qbxmlops120.py, it is encoded from utf8 in the first place
            # and since it is generated files, I don't want to mess up with that
            #return input_data.encode('ascii', 'xmlcharrefreplace')
            return input_data.decode('utf-8').encode('ascii', 'xmlcharrefreplace')
        except UnicodeDecodeError, e:
            # if still error, I'll ignore it for now
            return input_data.decode('utf-8').encode('ascii', 'ignore')

    def gds_validate_string(self, input_data, node, input_name=''):
        return input_data

    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % input_data

    def gds_validate_integer(self, input_data, node, input_name=''):
        return input_data

    def gds_format_integer_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_integer_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                fvalue = float(value)
            except (TypeError, ValueError), exp:
                raise_parse_error(node, 'Requires sequence of integers')
        return input_data

    def gds_format_float(self, input_data, input_name=''):
        return '%f' % input_data

    def gds_validate_float(self, input_data, node, input_name=''):
        return input_data

    def gds_format_float_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_float_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                fvalue = float(value)
            except (TypeError, ValueError), exp:
                raise_parse_error(node, 'Requires sequence of floats')
        return input_data

    def gds_format_double(self, input_data, input_name=''):
        return '%e' % input_data

    def gds_validate_double(self, input_data, node, input_name=''):
        return input_data

    def gds_format_double_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_double_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                fvalue = float(value)
            except (TypeError, ValueError), exp:
                raise_parse_error(node, 'Requires sequence of doubles')
        return input_data

    def gds_format_boolean(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_boolean(self, input_data, node, input_name=''):
        return input_data

    def gds_format_boolean_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_boolean_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            if value not in ('true', '1', 'false', '0', ):
                raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
        return input_data

    def gds_str_lower(self, instring):
        return instring.lower()

    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path

    Tag_strip_pattern_ = re_.compile(r'\{.*\}')

    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)

    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{%s}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1

    def gds_build_any(self, node, type_name=None):
        return None

    def to_dict(self):
        if not hasattr(self, "__dict__"):
            return None
        result = {}
        for (k,v) in self.__dict__.iteritems():
            if (v is None) or (v == []) or (v == {}):
                continue
            if hasattr(v, "to_dict"):
                result[k]=v.to_dict()
            elif isinstance(v, list):
                items = []
                for i in v:
                    if hasattr(i, "to_dict"):
                        items.append(i.to_dict())
                    elif isinstance(i, list):
                        continue # assume no list in list
                    elif isinstance(i, int) or isinstance(i, str) or isinstance(i, dict):
                        items.append(i)
                result[k]=items
            elif isinstance(v, int) or isinstance(v, str) or isinstance(v, dict):
                result[k]=v
            else:
                continue
        return result


