# vim: syntax=python:

top = '.'
out = 'build'

def options(opt):
	opt.load('compiler_d waf_unit_test')
	opt.recurse('scripts')
	opt.recurse('lib')
	opt.recurse('src')
	opt.recurse('test')
	opt.recurse('doc')

def configure(cnf):
	cnf.load('compiler_d waf_unit_test')
	cnf.env['DMACHL_SOURCE_DIR'] = [cnf.path.find_dir('src').abspath()] 
	cnf.env.append_value('INCLUDES', cnf.env['DMACHL_SOURCE_DIR'])
	cnf.env.append_value('DFLAGS', [])

	if cnf.env['COMPILER_D'] == 'dmd':
		cnf.env['DFLAGS_UNIT_TESTING'] = '-unittest'
		cnf.env['DFLAGS_DEBUG'] = '-g'
	elif cnf.env['COMPILER_D'] == 'gdc':
		cnf.env['DFLAGS_UNIT_TESTING'] = '-funittest'
		cnf.env['DFLAGS_DEBUG'] = '-g'
	elif cnf.env['COMPILER_D'] == 'ldc2':
		cnf.env['DFLAGS_UNIT_TESTING'] = '-unittest'
		cnf.env['DFLAGS_DEBUG'] = '-g'
	
	cnf.recurse('scripts')
	cnf.recurse('lib')
	cnf.recurse('src')
	cnf.recurse('test')
	cnf.recurse('doc')

def build(bld):
	bld.recurse('scripts')
	bld.recurse('lib')
	bld.recurse('src')
	bld.recurse('test')
	bld.recurse('doc')

	from waflib.Tools import waf_unit_test
	bld.add_post_fun(waf_unit_test.summary)

